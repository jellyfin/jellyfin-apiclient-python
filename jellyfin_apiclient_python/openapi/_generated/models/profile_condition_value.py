from enum import Enum


class ProfileConditionValue(str, Enum):
    AUDIOBITDEPTH = "AudioBitDepth"
    AUDIOBITRATE = "AudioBitrate"
    AUDIOCHANNELS = "AudioChannels"
    AUDIOPROFILE = "AudioProfile"
    AUDIOSAMPLERATE = "AudioSampleRate"
    HAS64BITOFFSETS = "Has64BitOffsets"
    HEIGHT = "Height"
    ISANAMORPHIC = "IsAnamorphic"
    ISAVC = "IsAvc"
    ISINTERLACED = "IsInterlaced"
    ISSECONDARYAUDIO = "IsSecondaryAudio"
    NUMAUDIOSTREAMS = "NumAudioStreams"
    NUMSTREAMS = "NumStreams"
    NUMVIDEOSTREAMS = "NumVideoStreams"
    PACKETLENGTH = "PacketLength"
    REFFRAMES = "RefFrames"
    VIDEOBITDEPTH = "VideoBitDepth"
    VIDEOBITRATE = "VideoBitrate"
    VIDEOCODECTAG = "VideoCodecTag"
    VIDEOFRAMERATE = "VideoFramerate"
    VIDEOLEVEL = "VideoLevel"
    VIDEOPROFILE = "VideoProfile"
    VIDEORANGETYPE = "VideoRangeType"
    VIDEOTIMESTAMP = "VideoTimestamp"
    WIDTH = "Width"

    def __str__(self) -> str:
        return str(self.value)
