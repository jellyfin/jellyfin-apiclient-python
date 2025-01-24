"""
Creates a demo jellyfin server using a container interface (e.g. podman or
docker). This is used for automated testing.
"""
import ubelt as ub


class DemoJellyfinServerManager():
    """
    Manages a demo jellyfin server.

    Has the ability to:

        * initialize a new a server

        * destroy an existing server

        * populate an server with demo data

        * check if a server exists

    Example:
        >>> from jellyfin_apiclient_python.demo.demo_jellyfin_server import *  # NOQA
        >>> demoman = DemoJellyfinServerManager()
        >>> demoman.verbose = 3
        >>> demoman.server_exists()
        >>> demoman.ensure_server(reset=True)
        >>> assert demoman.server_exists()
    """

    def __init__(self):
        # these can be parameterized in the future
        self.jellyfin_image_name = 'jellyfin/jellyfin'
        self.oci_container_name = 'jellyfin-apiclient-python-test-server'
        self.oci_exe = find_oci_exe()
        self.url = 'http://localhost'
        self.port = '8097'
        self.verbose = 3
        # This is where local demo media will be stored
        self.test_dpath = ub.Path.appdir('jellyfin-apiclient-python/demo/demo_server')
        self.media_dpath = (self.test_dpath / 'media').ensuredir()
        # cache_dpath = (test_dpath / 'cache').ensuredir()
        # config_dpath = (test_dpath / 'config').ensuredir()

    def ensure_server(self, reset=False):
        """
        Main entry point that will quickly check if a server exists, and if it
        does not it will set up a small one for testing purposes. By passing
        reset=True you can delete an existing server and force a fresh start.
        """
        if reset:
            self.teardown_existing_server()

        if not self.server_exists():
            self.initialize_new_server()
            self.ensure_local_demo_media()
            self.populate_demo_media()

    def server_exists(self):
        """
        Returns:
            bool: True there is a container running the jellyfin server
        """
        info = ub.cmd(f'{self.oci_exe} ps', verbose=self.verbose)
        return self.oci_container_name in info.stdout

    def teardown_existing_server(self):
        """
        Destroys any server if it exists.
        """
        ub.cmd(f'{self.oci_exe} stop {self.oci_container_name}', verbose=self.verbose)
        ub.cmd(f'{self.oci_exe} rm {self.oci_container_name}', verbose=self.verbose)

    def initialize_new_server(self):
        """
        Pulls the OCI image, starts a container running the image, and steps
        through the initialization procedure. This results in an initialized,
        but empty jellyfin server.
        """
        import time

        # Ensure we have the jellyfin container image.
        ub.cmd(f'{self.oci_exe} pull {self.jellyfin_image_name}', check=True)

        # Ensure the media path that we are mounting exists
        self.media_dpath.ensuredir()

        docker_args = [
            'docker', 'run',
            '--rm=true',
            '--detach=true',
            '--name', self.oci_container_name,
            '--publish', f'{self.port}:8096/tcp',
            # '--user', 'uid:gid',
            # Dont mount these so we start with a fresh database on docker
            # restart
            # '--volume', f'{cache_dpath}:/cache',
            # '--volume', f'{config_dpath}:/config',
            '--mount', f'type=bind,source={self.media_dpath},target=/media',
            # '--restart', 'unless-stopped',
            '--restart', 'no',
            'jellyfin/jellyfin',
        ]
        ub.cmd(docker_args, verbose=3, check=True)

        # Wait for the server to spin up.
        info = ub.cmd(f'{self.oci_exe} ps', verbose=self.verbose)
        while 'starting' in info.stdout:
            time.sleep(3)
            info = ub.cmd(f'{self.oci_exe} ps', verbose=self.verbose)

        # Programatically initialize the new server with a user with name
        # "jellyfin" and password "jellyfin". This process was discovered
        # by looking at what the webUI does, and isn't part of the core
        # jellyfin API, so it may break in the future.

        # References:
        # https://matrix.to/#/!YOoxJKhsHoXZiIHyBG:matrix.org/$H4ymY6TE0mtkVEaaxQDNosjLN7xXE__U_gy3u-FGPas?via=bonifacelabs.ca&via=t2bot.io&via=matrix.org
        import requests
        time.sleep(1)

        resp = requests.post(f'{self.url}:{self.port}/Startup/Configuration', json={"UICulture": "en-US", "MetadataCountryCode": "US", "PreferredMetadataLanguage": "en"})
        assert resp.ok
        time.sleep(1)

        resp = requests.get(f'{self.url}:{self.port}/Startup/User')
        assert resp.ok
        time.sleep(1)

        resp = requests.post(f'{self.url}:{self.port}/Startup/User', json={"Name": "jellyfin", "Password": "jellyfin"})
        assert resp.ok
        time.sleep(1)

        payload = {"UICulture": "en-US", "MetadataCountryCode": "US", "PreferredMetadataLanguage": "en"}
        resp = requests.post(f'{self.url}:{self.port}/Startup/Configuration', json=payload)
        assert resp.ok
        time.sleep(1)

        payload = {"EnableRemoteAccess": True, "EnableAutomaticPortMapping": False}
        resp = requests.post(f'{self.url}:{self.port}/Startup/RemoteAccess', json=payload)
        assert resp.ok
        time.sleep(1)

        resp = requests.post(f'{self.url}:{self.port}/Startup/Complete')
        assert resp.ok
        time.sleep(1)

    def ensure_local_demo_media(self):
        """
        Downloads permissive licensed media to the local host.
        These will be mounted on our demo jellyfin server.
        """
        media_dpath = self.media_dpath
        movies_dpath = (media_dpath / 'movies').ensuredir()
        music_dpath = (media_dpath / 'music').ensuredir()

        # TODO: fix bbb
        # zip_fpath = ub.grabdata('https://download.blender.org/demo/movies/BBB/bbb_sunflower_1080p_30fps_normal.mp4.zip',
        #                         dpath=movies_dpath,
        #                         hash_prefix='e320fef389ec749117d0c1583945039266a40f25483881c2ff0d33207e62b362',
        #                         hasher='sha256')
        # mp4_fpath = ub.Path(zip_fpath).augment(ext='')
        # if not mp4_fpath.exists():
        #     import zipfile
        #     zfile = zipfile.ZipFile(zip_fpath)
        #     zfile.extractall(path=media_dpath)

        ub.grabdata('https://tile.loc.gov/storage-services/service/mbrs/ntscrm/00068306/00068306.mp4', fname='Popeye the Sailor meets Sinbad the Sailor.mp4', dpath=movies_dpath)
        ub.grabdata('https://tile.loc.gov/storage-services/service/mbrs/ntscrm/00000765/00000765.mp4', fname='The great train robbery.mp4', dpath=movies_dpath)

        ub.grabdata('https://commons.wikimedia.org/wiki/File:Zur%C3%BCck_in_die_Zukunft_(Film)_01.ogg', fname='Zurück in die Zukunft.ogg', dpath=music_dpath)
        ub.grabdata('https://upload.wikimedia.org/wikipedia/commons/e/e1/Heart_Monitor_Beep--freesound.org.mp3', dpath=music_dpath)
        ub.grabdata('https://upload.wikimedia.org/wikipedia/commons/6/63/Clair_de_Lune_-_Wright_Brass_-_United_States_Air_Force_Band_of_Flight.mp3', dpath=music_dpath)
        ub.grabdata('https://upload.wikimedia.org/wikipedia/commons/7/73/Schoenberg_-_Drei_Klavierst%C3%BCcke_No._1_-_Irakly_Avaliani.webm', dpath=music_dpath)
        ub.grabdata('https://upload.wikimedia.org/wikipedia/commons/6/63/Clair_de_Lune_-_Wright_Brass_-_United_States_Air_Force_Band_of_Flight.mp3', dpath=music_dpath)

    def populate_demo_media(self):
        """
        Sends API calls to the server to add the demo media to the jellyfin
        database.
        """
        # Create a client to perform some initial configuration.
        from jellyfin_apiclient_python import JellyfinClient
        client = JellyfinClient()
        client.config.app(
            name='DemoServerMediaPopulator',
            version='0.1.0',
            device_name='machine_name',
            device_id='unique_id')
        client.config.data["auth.ssl"] = True
        url = f'{self.url}:{self.port}'
        username = 'jellyfin'
        password = 'jellyfin'
        client.auth.connect_to_address(url)
        client.auth.login(url, username, password)

        client.jellyfin.add_media_library(
            name='Movies', collectionType='movies',
            paths=['/media/movies'], refreshLibrary=True,
        )
        client.jellyfin.add_media_library(
            name='Music', collectionType='music',
            paths=['/media/music'], refreshLibrary=True,
        )


def find_oci_exe():
    """
    Search for docker or podman and return a path to the executable if it
    exists, otherwise raise an exception.
    """
    oci_exe = ub.find_exe('docker')
    if not oci_exe:
        oci_exe = ub.find_exe('podman')
    if oci_exe is None:
        raise Exception('Docker / podman is required')
    return oci_exe
