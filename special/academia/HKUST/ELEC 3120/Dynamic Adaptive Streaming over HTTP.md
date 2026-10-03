---
aliases:
  - DASH
  - Dynamic Adaptive Streaming over HTTP
  - ELEC 3120 Dynamic Adaptive Streaming over HTTP
  - ELEC3120 Dynamic Adaptive Streaming over HTTP
  - HKUST ELEC 3120 Dynamic Adaptive Streaming over HTTP
  - HKUST ELEC3120 Dynamic Adaptive Streaming over HTTP
  - MPEG-DASH
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/Dynamic_Adaptive_Streaming_over_HTTP
  - language/in/English
---

# Dynamic Adaptive Streaming over HTTP

DASH streams a video over HTTP requests for ordinary files. A quality level in a DASH manifest is one bitrate and one resolution. Nothing in the protocol says which level to ask for. The case for chunking a video at all belongs to [media segmentation](media%20segmentation.md#why%20http%20took%20over).

---

Flashcards for this section are as follows:

- what does DASH change about the way a video is served? ::@:: Nothing about the transport. DASH uses ordinary HTTP requests for ordinary files

## the manifest

The client opens a session by asking for a manifest file, and the reply is an ordinary file. That file is the media presentation description (MPD), an XML document. Its details need not be memorised, because three element names give it its shape.

An `AdaptationSet` holds one stream, video or audio. A `SegmentTemplate` gives the rule for finding a segment of that stream. A `Representation` is one quality level of that stream.

---

Flashcards for this section are as follows:

- what does an `AdaptationSet` hold? ::@:: One stream, video or audio
- what does a `SegmentTemplate` give? ::@:: The rule for finding a segment of that stream
- what is a `Representation`? ::@:: One quality level of that stream
- what can a client do once it has read the manifest? ::@:: Address any segment in the presentation by name

## what this manifest contains

The presentation is static and in the ISO main profile. It runs 3 minutes 30 seconds, with a `minBufferTime` of 1 second. It holds a single `Period`, and inside that one `AdaptationSet` for video and one for audio.

<!-- check: ignore-file[math_in_code_fence]: $RepresentationID$ and $Number$ are DASH template macros written with dollar signs, not LaTeX  -->
```xml
<MPD id="f08e80da-bf1d-4e3d-8899-f0f6155f6efa"
     profiles="urn:mpeg:dash:profile:isoff-main:2011" type="static"
     mediaPresentationDuration="P0Y0M0DT0H3M30.000S"
     minBufferTime="P0Y0M0DT0H0M1.000S"
     xmlns="urn:mpeg:dash:schema:mpd:2011"
     xmlns:bitmovin="http://www.bitmovin.net/mpd/2015">
  <Period>
    <AdaptationSet mimeType="video/mp4" codecs="avc1.42c00d">
      <SegmentTemplate media="../video/$RepresentationID$/dash/segment_$Number$.m4s"
                       initialization="../video/$RepresentationID$/dash/init.mp4"
                       duration="100000" startNumber="0" timescale="25000"/>
      <Representation id="180_250000"   bandwidth="250000"  width="320"  height="180" frameRate="25"/>
      <Representation id="270_400000"   bandwidth="400000"  width="480"  height="270" frameRate="25"/>
      <Representation id="360_800000"   bandwidth="800000"  width="640"  height="360" frameRate="25"/>
      <Representation id="540_1200000"  bandwidth="1200000" width="960"  height="540" frameRate="25"/>
      <Representation id="720_2400000"  bandwidth="2400000" width="1280" height="720" frameRate="25"/>
      <Representation id="1080_4800000" bandwidth="4800000" width="1920" height="1080" frameRate="25"/>
    </AdaptationSet>
    <AdaptationSet lang="en" mimeType="audio/mp4" codecs="mp4a.40.2" bitmovin:label="English stereo">
      <SegmentTemplate media="../audio/$RepresentationID$/dash/segment_$Number$.m4s"
                       initialization="../audio/$RepresentationID$/dash/init.mp4"
                       duration="191472" startNumber="0" timescale="48000"/>
      <Representation id="1_stereo_128000" bandwidth="128000" audioSamplingRate="48000"/>
    </AdaptationSet>
  </Period>
</MPD>
```

The video `AdaptationSet` opens with its `SegmentTemplate`, which gives the URI of any segment in that stream. The template substitutes `$RepresentationID$` for the chosen level and `$Number$` for the segment's index. Its `initialization` attribute points at the `init.mp4` file a client fetches before any segment.

The six `Representation` elements give six quality levels of the same video, from 250 kbps at 320x180 to 4.8 Mbps at 1920x1080, all at a frame rate of 25. Each `id` encodes the height and the bandwidth, as `1080_4800000` for the 1080p entry at 4.8 Mbps.

The audio `AdaptationSet` repeats the same structure for one stereo track at 128 kbps and $48000\,\mathrm{Hz}$. Audio is fetched and decoded separately from the video.

---

Flashcards for this section are as follows:

- what does the `SegmentTemplate` element do? ::@:: It gives the URI of any segment, substituting `$RepresentationID$` for the level and `$Number$` for the segment index <!-- check: ignore-line[two_sided_calc_warning]: conceptual, the symbols are DASH template names and the card asks what the element does, not for a computed value -->
- what does a `Representation` `id` encode? ::@:: The height and the bandwidth, as `1080_4800000` for the 1080p entry at 4.8 Mbps
- how is the audio track fetched and decoded? ::@:: Separately from the video

## what the player does

The client now chooses which segments to fetch. The ABR algorithm makes that choice, and the protocol takes no part in it. Choosing well is the subject of [adaptive bitrate streaming](adaptive%20bitrate%20streaming.md).

The [Dash JavaScript Player](https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html) is the reference implementation, and its sample page runs a real presentation in a browser.

---

Flashcards for this section are as follows:

- which part of a DASH session chooses which segments to fetch? ::@:: The ABR algorithm
- which reference implementation of DASH runs a presentation in a browser? ::@:: The Dash JavaScript Player (dash.js)
