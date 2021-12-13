<div align="center">

# YTDL-PATCHED
A command-line program to download videos from YouTube and many other [video platforms](supportedsites.md)

</div>

## MIRRORS
- ~~https://github.com/nao20010128nao/ytdl-patched (passed away)~~
- https://github.com/ytdl-patched/ytdl-patched (primary)
- https://bitbucket.org/nao20010128nao/ytdl-patched (secondary)
- https://forge.tedomum.net/nao20010128nao/ytdl-patched (secondary)
- https://gitlab.com/lesmi_the_goodness/ytdl-patched (secondary)
- https://gitea.com/nao20010128nao/ytdl-patched (secondary)
- https://git.sr.ht/~nao20010128nao/ytdl-patched (secondary)
  - manually mirrored at every git push
- https://codeberg.org/nao20010128nao/ytdl-patched (secondary)
- https://gitgud.io/nao20010128nao/ytdl-patched (secondary)
- [In my Keybase account](https://book.keybase.io/git) (secondary)
  - spoiler: you can clone it with `git clone keybase://public/nao20010128nao/ytdl-patched`
- https://bookish-octo-barnacle.vercel.app/ (just for fun, no longer synced)
- https://ytdl-patched.netlify.app/ (just for fun, no longer synced)

<!-- MARKER BEGIN -->

| Service | Type | Status | Note |
|:-------:|:----:|:------:|:----:|
| Travis CI | Tests | [![Build Status](https://travis-ci.org/nao20010128nao/ytdl-patched.svg?branch=master)](https://travis-ci.org/nao20010128nao/ytdl-patched.svg) | Stopped because of lack of credits |
| GitHub Actions | Tests | [![Run tests](https://github.com/ytdl-patched/ytdl-patched/actions/workflows/tests.yml/badge.svg?branch=ytdlp)](https://github.com/ytdl-patched/ytdl-patched/actions/workflows/tests.yml) | |
| GitHub Actions | Build and release | [![Build Patched YTDL](https://github.com/ytdl-patched/ytdl-patched/actions/workflows/build.yml/badge.svg?branch=ytdlp)](https://github.com/ytdl-patched/ytdl-patched/actions/workflows/build.yml) | |
| GitHub Actions | Merging commits from upstream | [![Merge upstream](https://github.com/ytdl-patched/ytdl-patched/actions/workflows/merge.yml/badge.svg?branch=ytdlp)](https://github.com/ytdl-patched/ytdl-patched/actions/workflows/merge.yml) | There's conflict if it fails |

<!-- MARKER END -->

ytdl-patched is a [youtube-dl](https://github.com/ytdl-org/youtube-dl) fork based on [yt-dlp](https://github.com/yt-dlp/yt-dlp).

* [NEW FEATURES](#new-features)
    * [NEW FEATURES IN YTDL-PATCHED](#new-features-in-ytdl-patched)
    * [NEW FEATURES IN YT-DLP](#new-features-in-yt-dlp)
    * [Differences in default behavior](#differences-in-default-behavior)
* [INSTALLATION](#installation)
    * [Update](#update)
    * [Dependencies](#dependencies)
    * [Compile](#compile)
* [USAGE AND OPTIONS](#usage-and-options)
    * [General Options](#general-options)
    * [Network Options](#network-options)
    * [Geo-restriction](#geo-restriction)
    * [Video Selection](#video-selection)
    * [Download Options](#download-options)
    * [Filesystem Options](#filesystem-options)
    * [Thumbnail Options](#thumbnail-options)
    * [Internet Shortcut Options](#internet-shortcut-options)
    * [Verbosity and Simulation Options](#verbosity-and-simulation-options)
    * [Workarounds](#workarounds)
    * [Video Format Options](#video-format-options)
    * [Subtitle Options](#subtitle-options)
    * [Authentication Options](#authentication-options)
    * [Post-processing Options](#post-processing-options)
    * [SponsorBlock Options](#sponsorblock-options)
    * [Extractor Options](#extractor-options)
* [CONFIGURATION](#configuration)
    * [Authentication with .netrc file](#authentication-with-netrc-file)
* [OUTPUT TEMPLATE](#output-template)
    * [Output template and Windows batch files](#output-template-and-windows-batch-files)
    * [Output template examples](#output-template-examples)
* [FORMAT SELECTION](#format-selection)
    * [Filtering Formats](#filtering-formats)
    * [Sorting Formats](#sorting-formats)
    * [Format Selection examples](#format-selection-examples)
* [MODIFYING METADATA](#modifying-metadata)
    * [Modifying metadata examples](#modifying-metadata-examples)
* [EXTRACTOR ARGUMENTS](#extractor-arguments)
* [PLUGINS](#plugins)
* [EMBEDDING YT-DLP](#embedding-yt-dlp)
* [DEPRECATED OPTIONS](#deprecated-options)
* [CONTRIBUTING](CONTRIBUTING.md#contributing-to-yt-dlp)
    * [Opening an Issue](CONTRIBUTING.md#opening-an-issue)
    * [Developer Instructions](CONTRIBUTING.md#developer-instructions)
* [MORE](#more)

# NEW FEATURES
## NEW FEATURES IN YTDL-PATCHED
The major new features from the latest release of [yt-dlp](https://github.com/yt-dlp/yt-dlp) are:

* **Long name escaping for Unix systems**: If the filename of downloaded videos can get longer than 255 bytes (in system locale), it'll prevent from exceeding its length by splitting in 255 bytes each. Note that treating splitted names requires special scripts just for that.

* **Generic Extractor will not return at first website match**: Generic Extractor collects matched websites and return it as playlist. It creates nested playlist and may cause infinite loop.

* **Generic Extractor Extended**
    * Following URLs are resolved and redirect automatically to its destination.
        * Japanese BBS redirect: `pinktower.com`, `jump.5ch.net`, `jump.megabbs.info`
        * Pixiv redirect
            * Looking for test cases for char-mutated URLs
        * Firebase Dynamic Link: domains ending with `.page.link`
    * Self-hosted service support (Mastodon, PeerTube and Misskey)
        * For supported self-hosted services, ytdl-patched contains a huge list of instances. But you can opt-in for instance checking, in case of undiscovered instance.  To opt-in, use these flags: `--check-mastodon-instance`, `--check-peertube-instance`, `--check-misskey-instance`

* ~~**More YouTube improvements**~~:
    * More rate-limit bypass attempt: decrypting `n` params using external service I've made (as fallback after yt-dlp/yt-dlp#1437 is merged)

* **NicoNico comments as subtitles**: Now you can download NicoNico comments as a subtitle.
    * No dependency required. Just use ytdl-patched.
    * Minimum flags: `--sub-format ass --write-subs`
    * To embed comments without problems: `--sub-format ass --write-subs --embed-subs --remux-video mkv`

* **New extractors**: Following extractors have been added: (broken/imcomplete ones not listed here)
    * `AbemaTV` and `AbemaTVTitle`
    * `askmona` and `askmona3` (just scrapes embedded YouTube videos)
    * `disneychris`
    * `dnatube`
    * `fc2:user` (FC2 user-uploaded videos)
    * `iwara:user` (Iwara user-uploaded videos)
    * `javhub`
    * `peing`, `ask.fm`, `marshmallow-qa`, `mottohomete` (scrapes Q&A section and find video URLs in it)
    * `mastodon`, `mastodon:user`, `mastodon:user:numeric_id`
    * `misskey`, `misskey:user`
    * `niconico:live` (**COMMENTS ARE NOT SUPPORTED**)
    * `niconico:playlist`, `niconico:series`, `niconico:user`
    * `pixiv:sketch`, `pixiv:sketch:user`
    * `sharevideos`
    * `tokyomotion`, `tokyomotion:searches`, `tokyomotion:user`, `tokyomotion:user:favs`
    * `NhkForSchoolBangumiIE`, `NhkForSchoolSubjectIE`, `NhkForSchoolProgramListIE` (NHK for School)
    * `mixch` (merged in upstream)
    * `skeb` (merged in upstream)
    * `mirrativ`, `mirrativ:user` (merged in upstream)
    * `openrec`, `openrec:capture` (merged in upstream)
    * `Radiko`, `RadikoRadio` (does not have 24-hours limitation!) (merged in upstream)
    * `voicy`, `voicy:channel` (merged in upstream)
    * `whowatch` (merged in upstream)
    * `damtomo:video`, `damtomo:record` (merged in upstream)
    * `17live`, `17live:clip` (merged in upstream)

* **Some features/behaviors are reverted**: Some changes in yt-dlp has been reverted to match that of youtube-dl.
    * Output filename template. In yt-dlp, it was `%(title)s [%(id)s].%(ext)s`. But ytdl-patched uses `%(title)s-%(id)s.%(ext)s`.

* **New extractor arguments**: Some extractor arguments are added. Check [**EXTRACTOR ARGUMENTS**](#extractor-arguments) section for details.

* **Merging**: MKV file is preferred for merging, but can be overriden using `--merge-output-format`. ytdl-patched does not determine merge format from downloaded formats.

* **Format debugger**: You can debug `-f FORMAT` specs, by just adding `-Fv`. This doesn't work if specs passed to `-f` is malformed.
You'll get `DEBUG` column with tokens in arguments, and list of unmatched tokens.


## NEW FEATURES IN YT-DLP
* Based on **youtube-dl 2021.06.06 [commit/379f52a](https://github.com/ytdl-org/youtube-dl/commit/379f52a4954013767219d25099cce9e0f9401961)** and **youtube-dlc 2020.11.11-3 [commit/98e248f](https://github.com/blackjack4494/yt-dlc/commit/98e248faa49e69d795abc60f7cdefcf91e2612aa)**: You get all the features and patches of [youtube-dlc](https://github.com/blackjack4494/yt-dlc) in addition to the latest [youtube-dl](https://github.com/ytdl-org/youtube-dl)

* **[SponsorBlock Integration](#sponsorblock-options)**: You can mark/remove sponsor sections in youtube videos by utilizing the [SponsorBlock](https://sponsor.ajay.app) API

* **[Format Sorting](#sorting-formats)**: The default format sorting options have been changed so that higher resolution and better codecs will be now preferred instead of simply using larger bitrate. Furthermore, you can now specify the sort order using `-S`. This allows for much easier format selection than what is possible by simply using `--format` ([examples](#format-selection-examples))

* **Merged with animelover1984/youtube-dl**: You get most of the features and improvements from [animelover1984/youtube-dl](https://github.com/animelover1984/youtube-dl) including `--write-comments`, `BiliBiliSearch`, `BilibiliChannel`, Embedding thumbnail in mp4/ogg/opus, playlist infojson etc. Note that the NicoNico improvements are not available. See [#31](https://github.com/yt-dlp/yt-dlp/pull/31) for details.

* **Youtube improvements**:
    * All Feeds (`:ytfav`, `:ytwatchlater`, `:ytsubs`, `:ythistory`, `:ytrec`) and private playlists supports downloading multiple pages of content
    * Search (`ytsearch:`, `ytsearchdate:`), search URLs and in-channel search works
    * Mixes supports downloading multiple pages of content
    * Some (but not all) age-gated content can be downloaded without cookies
    * Fix for [n-sig based throttling](https://github.com/ytdl-org/youtube-dl/issues/29326)
    * Redirect channel's home URL automatically to `/video` to preserve the old behaviour
    * `255kbps` audio is extracted (if available) from youtube music when premium cookies are given
    * Youtube music Albums, channels etc can be downloaded ([except self-uploaded music](https://github.com/yt-dlp/yt-dlp/issues/723))

* **Cookies from browser**: Cookies can be automatically extracted from all major web browsers using `--cookies-from-browser BROWSER[:PROFILE]`

* **Split video by chapters**: Videos can be split into multiple files based on chapters using `--split-chapters`

* **Multi-threaded fragment downloads**: Download multiple fragments of m3u8/mpd videos in parallel. Use `--concurrent-fragments` (`-N`) option to set the number of threads used

* **Aria2c with HLS/DASH**: You can use `aria2c` as the external downloader for DASH(mpd) and HLS(m3u8) formats

* **New and fixed extractors**: Many new extractors have been added and a lot of exisiting ones have been fixed. See the [changelog](Changelog.md) or the [list of supported sites](supportedsites.md)

* **New MSOs**: Philo, Spectrum, SlingTV, Cablevision, RCN

* **Subtitle extraction from manifests**: Subtitles can be extracted from streaming media manifests. See [commit/be6202f](https://github.com/yt-dlp/yt-dlp/commit/be6202f12b97858b9d716e608394b51065d0419f) for details

* **Multiple paths and output templates**: You can give different [output templates](#output-template) and download paths for different types of files. You can also set a temporary path where intermediary files are downloaded to using `--paths` (`-P`)

* **Portable Configuration**: Configuration files are automatically loaded from the home and root directories. See [configuration](#configuration) for details

* **Output template improvements**: Output templates can now have date-time formatting, numeric offsets, object traversal etc. See [output template](#output-template) for details. Even more advanced operations can also be done with the help of `--parse-metadata` and `--replace-in-metadata`

* **Other new options**: Many new options have been added such as `--print`, `--wait-for-video`, `--sleep-requests`, `--convert-thumbnails`, `--write-link`, `--force-download-archive`, `--force-overwrites`, `--break-on-reject` etc

* **Improvements**: Regex and other operators in `--match-filter`, multiple `--postprocessor-args` and `--downloader-args`, faster archive checking, more [format selection options](#format-selection), merge multi-video/audio etc

* **Plugins**: Extractors and PostProcessors can be loaded from an external file. See [plugins](#plugins) for details

* **Self-updater**: The releases can be updated using `yt-dlp -U`

See [changelog](Changelog.md) or [commits](https://github.com/yt-dlp/yt-dlp/commits) for the full list of changes

### Differences in default behavior

Some of yt-dlp's default options are different from that of youtube-dl and youtube-dlc: (Some of them also be reverted in ytdl-patched)

* The options `--id`, `--auto-number` (`-A`), `--title` (`-t`) and `--literal` (`-l`), no longer work. See [removed options](#Removed) for details
* `avconv` is not supported as as an alternative to `ffmpeg`
* ~~The default [output template](#output-template) is `%(title)s [%(id)s].%(ext)s`. There is no real reason for this change. This was changed before yt-dlp was ever made public and now there are no plans to change it back to `%(title)s.%(id)s.%(ext)s`. Instead, you may use `--compat-options filename`~~ **This is reverted in ytdl-patched to keep consistent with old versions. See above.**
* The default [format sorting](#sorting-formats) is different from youtube-dl and prefers higher resolution and better codecs rather than higher bitrates. You can use the `--format-sort` option to change this to any order you prefer, or use `--compat-options format-sort` to use youtube-dl's sorting order
* The default format selector is `bv*+ba/b`. This means that if a combined video + audio format that is better than the best video-only format is found, the former will be prefered. Use `-f bv+ba/b` or `--compat-options format-spec` to revert this
* Unlike youtube-dlc, yt-dlp does not allow merging multiple audio/video streams into one file by default (since this conflicts with the use of `-f bv*+ba`). If needed, this feature must be enabled using `--audio-multistreams` and `--video-multistreams`. You can also use `--compat-options multistreams` to enable both
* `--ignore-errors` is enabled by default. Use `--abort-on-error` or `--compat-options abort-on-error` to abort on errors instead
* When writing metadata files such as thumbnails, description or infojson, the same information (if available) is also written for playlists. Use `--no-write-playlist-metafiles` or `--compat-options no-playlist-metafiles` to not write these files
* `--add-metadata` attaches the `infojson` to `mkv` files in addition to writing the metadata when used with `--write-info-json`. Use `--no-embed-info-json` or `--compat-options no-attach-info-json` to revert this
* Some metadata are embedded into different fields when using `--add-metadata` as compared to youtube-dl. Most notably, `comment` field contains the `webpage_url` and `synopsis` contains the `description`. You can [use `--parse-metadata`](https://github.com/yt-dlp/yt-dlp#modifying-metadata) to modify this to your liking or use `--compat-options embed-metadata` to revert this
* `playlist_index` behaves differently when used with options like `--playlist-reverse` and `--playlist-items`. See [#302](https://github.com/yt-dlp/yt-dlp/issues/302) for details. You can use `--compat-options playlist-index` if you want to keep the earlier behavior
* The output of `-F` is listed in a new format. Use `--compat-options list-formats` to revert this
* All *experiences* of a funimation episode are considered as a single video. This behavior breaks existing archives. Use `--compat-options seperate-video-versions` to extract information from only the default player
* Youtube live chat (if available) is considered as a subtitle. Use `--sub-langs all,-live_chat` to download all subtitles except live chat. You can also use `--compat-options no-live-chat` to prevent live chat from downloading
* Youtube channel URLs are automatically redirected to `/video`. Append a `/featured` to the URL to download only the videos in the home page. If the channel does not have a videos tab, we try to download the equivalent `UU` playlist instead. Also, `/live` URLs raise an error if there are no live videos instead of silently downloading the entire channel. You may use `--compat-options no-youtube-channel-redirect` to revert all these redirections
* Unavailable videos are also listed for youtube playlists. Use `--compat-options no-youtube-unavailable-videos` to remove this
* If `ffmpeg` is used as the downloader, the downloading and merging of formats happen in a single step when possible. Use `--compat-options no-direct-merge` to revert this
* Thumbnail embedding in `mp4` is done with mutagen if possible. Use `--compat-options embed-thumbnail-atomicparsley` to force the use of AtomicParsley instead
* Some private fields such as filenames are removed by default from the infojson. Use `--no-clean-infojson` or `--compat-options no-clean-infojson` to revert this
* When `--embed-subs` and `--write-subs` are used together, the subtitles are written to disk and also embedded in the media file. You can use just `--embed-subs` to embed the subs and automatically delete the seperate file. See [#630 (comment)](https://github.com/yt-dlp/yt-dlp/issues/630#issuecomment-893659460) for more info. `--compat-options no-keep-subs` can be used to revert this

For ease of use, a few more compat options are available:
* `--compat-options all`: Use all compat options
* `--compat-options youtube-dl`: Same as `--compat-options all,-multistreams`
* `--compat-options youtube-dlc`: Same as `--compat-options all,-no-live-chat,-no-youtube-channel-redirect`

### GOALS
- keep merging with [`yt-dlp/yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- implement miscellaneous extractors as possible
- make `-U` work (yes, really works)
- do anything best

### NOT TO DO
- don't change very much from yt-dlp

# INSTALLATION

You can install yt-dlp using one of the following methods:

### Using the release binary

You can simply download the [correct binary file](#release-files) for your OS: **[[Windows](https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/youtube-dl-red.exe)] [[UNIX-like](https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/youtube-dl)]**

In UNIX-like OSes (MacOS, Linux, BSD), you can also install the same in one of the following ways:

```
sudo curl -L https://bookish-octo-barnacle.vercel.app/api/release/latest/youtube-dl -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

```
sudo wget https://bookish-octo-barnacle.vercel.app/api/release/latest/youtube-dl -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

```
sudo aria2c https://bookish-octo-barnacle.vercel.app/api/release/latest/youtube-dl -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

PS: The manpages, shell completion files etc. are available in [yt-dlp.tar.gz](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.tar.gz)

### With [PIP](https://pypi.org/project/pip)

You can install the [PyPI package](https://pypi.org/project/yt-dlp) with:
```
python3 -m pip install -U yt-dlp
```

You can install without any of the optional dependencies using:
```
python3 -m pip install --no-deps -U yt-dlp
```

If you want to be on the cutting edge, you can also install the master branch with:
```
python3 -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.zip
```

Note that on some systems, you may need to use `py` or `python` instead of `python3`

### With [Homebrew](https://brew.sh)

macOS or Linux users that are using Homebrew can also install it by:

```
brew install nao20010128nao/my/ytdl-patched
```

## UPDATE
You can use `yt-dlp -U` to update if you are [using the provided release](#using-the-release-binary)

If you [installed with pip](#with-pip), simply re-run the same command that was used to install the program

If you [installed using Homebrew](#with-homebrew), run `brew upgrade nao20010128nao/my/ytdl-patched`

## RELEASE FILES

#### Recommended

File|Description
:---|:---
[youtube-dl](https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/youtube-dl)|Platform-independant binary. Needs Python (recommended for **UNIX-like systems**)
[youtube-dl-red.exe](https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/yt-dlp.exe)|Windows (Win7 SP1+) standalone x64 binary (recommended for **Windows**)

#### Alternatives

#### Misc

File|Description
:---|:---
[youtube-dl.tar.gz](https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/yt-dlp.tar.gz)|Source tarball. Also contains manpages, completions, etc
[yt_dlp-py2.py3-none-any.whl](https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/yt-dlp.tar.gz)|pip wheel for installation using pip
[yt_dlp-wheel.tar.gz](https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/yt-dlp.tar.gz)|pip .tar.gz for installation using pip


## DEPENDENCIES
Python versions 3.6+ (CPython and PyPy) are supported. Other versions and implementations may or may not work correctly.

<!-- Python 3.5+ uses VC++14 and it is already embedded in the binary created
<!x-- https://www.microsoft.com/en-us/download/details.aspx?id=26999 --x>
On windows, [Microsoft Visual C++ 2010 SP1 Redistributable Package (x86)](https://download.microsoft.com/download/1/6/5/165255E7-1014-4D0A-B094-B6A430A6BFFC/vcredist_x86.exe) is also necessary to run yt-dlp. You probably already have this, but if the executable throws an error due to missing `MSVCR100.dll` you need to install it manually.
-->

While all the other dependancies are optional, `ffmpeg` and `ffprobe` are highly recommended
* [**ffmpeg** and **ffprobe**](https://www.ffmpeg.org) - Required for [merging seperate video and audio files](#format-selection) as well as for various [post-processing](#post-processing-options) tasks. Licence [depends on the build](https://www.ffmpeg.org/legal.html)
* [**mutagen**](https://github.com/quodlibet/mutagen) - For embedding thumbnail in certain formats. Licenced under [GPLv2+](https://github.com/quodlibet/mutagen/blob/master/COPYING)
* [**pycryptodomex**](https://github.com/Legrandin/pycryptodome) - For decrypting AES-128 HLS streams and various other data. Licenced under [BSD2](https://github.com/Legrandin/pycryptodome/blob/master/LICENSE.rst)
* [**websockets**](https://github.com/aaugustin/websockets) - For downloading over websocket. Licenced under [BSD3](https://github.com/aaugustin/websockets/blob/main/LICENSE)
* [**keyring**](https://github.com/jaraco/keyring) - For decrypting cookies of chromium-based browsers on Linux. Licenced under [MIT](https://github.com/jaraco/keyring/blob/main/LICENSE)
* [**AtomicParsley**](https://github.com/wez/atomicparsley) - For embedding thumbnail in mp4/m4a if mutagen is not present. Licenced under [GPLv2+](https://github.com/wez/atomicparsley/blob/master/COPYING)
* [**rtmpdump**](http://rtmpdump.mplayerhq.hu) - For downloading `rtmp` streams. ffmpeg will be used as a fallback. Licenced under [GPLv2+](http://rtmpdump.mplayerhq.hu)
* [**mplayer**](http://mplayerhq.hu/design7/info.html) or [**mpv**](https://mpv.io) - For downloading `rstp` streams. ffmpeg will be used as a fallback. Licenced under [GPLv2+](https://github.com/mpv-player/mpv/blob/master/Copyright)
* [**phantomjs**](https://github.com/ariya/phantomjs) - Used in extractors where javascript needs to be run. Licenced under [BSD3](https://github.com/ariya/phantomjs/blob/master/LICENSE.BSD)
* [**js2py**](https://github.com/PiotrDabkowski/Js2Py) - Used in extractors where javascript needs to be run. Licenced under [MIT](https://github.com/PiotrDabkowski/Js2Py/blob/master/LICENSE.md)
* [**sponskrub**](https://github.com/faissaloo/SponSkrub) - For using the now **deprecated** [sponskrub options](#sponskrub-options). Licenced under [GPLv3+](https://github.com/faissaloo/SponSkrub/blob/master/LICENCE.md)
* Any external downloader that you want to use with `--downloader`

To use or redistribute the dependencies, you must agree to their respective licensing terms.

The Windows and MacOS standalone release binaries are already built with the python interpreter, mutagen, pycryptodomex and websockets included.

**Note**: There are some regressions in newer ffmpeg versions that causes various issues when used alongside yt-dlp. Since ffmpeg is such an important dependancy, we provide [custom builds](https://github.com/yt-dlp/FFmpeg-Builds/wiki/Latest#latest-autobuilds) with patches for these issues at [yt-dlp/FFmpeg-Builds](https://github.com/yt-dlp/FFmpeg-Builds). See [the readme](https://github.com/yt-dlp/FFmpeg-Builds#patches-applied) for details on the specifc issues solved by these builds


## COMPILE

**For Windows**:
To build the Windows executable, you must have pyinstaller (and optionally mutagen, pycryptodomex, websockets)

Once you have all the necessary dependencies installed, just run `pyinst.py`. The executable will be built for the same architecture (32/64 bit) as the python used to build it.

    py -m pip install -U pyinstaller -r requirements.txt
    py pyinst.py

Note that pyinstaller [does not support](https://github.com/pyinstaller/pyinstaller#requirements-and-tested-platforms) Python installed from the Windows store without using a virtual environment

**For Unix**:
You will need the required build tools: `python`, `make` (GNU), `pandoc`, `zip`, `pytest`  
Then simply run `make`. You can also run `make yt-dlp` instead to compile only the binary without updating any of the additional files

**Note**: In either platform, `devscripts\update-version.py` can be used to automatically update the version number

You can also fork the project on github and run your fork's [build workflow](.github/workflows/build.yml) to automatically build a release

# USAGE AND OPTIONS

    yt-dlp [OPTIONS] [--] URL [URL...]

`Ctrl+F` is your friend :D
<!-- Auto generated -->

## General Options:
    -h, --help                       Print this help text and exit
    --version                        Print program version and exit
    -U, --update                     Update this program to latest version. Make
                                     sure that you have sufficient permissions
                                     (run with sudo if needed)
    -i, --ignore-errors              Ignore download and postprocessing errors.
                                     The download will be considered successful
                                     even if the postprocessing fails
    --no-abort-on-error              Continue with next video on download
                                     errors; e.g. to skip unavailable videos in
                                     a playlist (default)
    --abort-on-error                 Abort downloading of further videos if an
                                     error occurs (Alias: --no-ignore-errors)
    --dump-user-agent                Display the current user-agent and exit
    --list-extractors                List all supported extractors and exit
    --extractor-descriptions         Output descriptions of all supported
                                     extractors and exit
    --force-generic-extractor        Force extraction to use the generic
                                     extractor
    --default-search PREFIX          Use this prefix for unqualified URLs. For
                                     example "gvsearch2:" downloads two videos
                                     from google videos for the search term
                                     "large apple". Use the value "auto" to let
                                     yt-dlp guess ("auto_warning" to emit a
                                     warning when guessing). "error" just throws
                                     an error. The default value "fixup_error"
                                     repairs broken URLs, but emits an error if
                                     this is not possible instead of searching
    --ignore-config                  Disable loading any configuration files
                                     except the one provided by --config-
                                     location. When given inside a configuration
                                     file, no further configuration files are
                                     loaded. Additionally, (for backward
                                     compatibility) if this option is found
                                     inside the system configuration file, the
                                     user configuration is not loaded
    --config-location PATH           Location of the main configuration file;
                                     either the path to the config or its
                                     containing directory
    --flat-playlist                  Do not extract the videos of a playlist,
                                     only list them
    --no-flat-playlist               Extract the videos of a playlist
    --wait-for-video MIN[-MAX]       Wait for scheduled streams to become
                                     available. Pass the minimum number of
                                     seconds (or range) to wait between retries
    --no-wait-for-video              Do not wait for scheduled streams (default)
    --mark-watched                   Mark videos watched (even with --simulate).
                                     Currently only supported for YouTube
    --no-mark-watched                Do not mark videos watched (default)
    --no-colors                      Do not emit color codes in output
    --compat-options OPTS            Options that can help keep compatibility
                                     with youtube-dl or youtube-dlc
                                     configurations by reverting some of the
                                     changes made in yt-dlp. See "Differences in
                                     default behavior" for details
    --check-mastodon-instance        Always perform online checks for Mastodon-
                                     like URL
    --check-peertube-instance        Always perform online checks for PeerTube-
                                     like URL
    --test-filename CMD              Like --exec option, but used for testing if
                                     downloading should be started. You can
                                     begin with "re:" to use regex instead of
                                     commands
    --print-infojson-types           DO NOT USE. IT'S MEANINGLESS FOR MOST
                                     PEOPLE. Prints types of object in info
                                     json. Use this for extractors that --print-
                                     json won' work.
    --enable-lock                    Locks downloading exclusively. Blocks other
                                     ytdl-patched process downloading the same
                                     video.
    --no-lock                        Do not lock downloading exclusively.
                                     Download will start even if other process
                                     is working on it.

## Network Options:
    --proxy URL                      Use the specified HTTP/HTTPS/SOCKS proxy.
                                     To enable SOCKS proxy, specify a proper
                                     scheme. For example
                                     socks5://127.0.0.1:1080/. Pass in an empty
                                     string (--proxy "") for direct connection
    --socket-timeout SECONDS         Time to wait before giving up, in seconds
    --source-address IP              Client-side IP address to bind to
    -4, --force-ipv4                 Make all connections via IPv4
    -6, --force-ipv6                 Make all connections via IPv6

## Geo-restriction:
    --geo-verification-proxy URL     Use this proxy to verify the IP address for
                                     some geo-restricted sites. The default
                                     proxy specified by --proxy (or none, if the
                                     option is not present) is used for the
                                     actual downloading
    --geo-bypass                     Bypass geographic restriction via faking
                                     X-Forwarded-For HTTP header
    --no-geo-bypass                  Do not bypass geographic restriction via
                                     faking X-Forwarded-For HTTP header
    --geo-bypass-country CODE        Force bypass geographic restriction with
                                     explicitly provided two-letter ISO 3166-2
                                     country code
    --geo-bypass-ip-block IP_BLOCK   Force bypass geographic restriction with
                                     explicitly provided IP block in CIDR
                                     notation

## Video Selection:
    --playlist-start NUMBER          Playlist video to start at (default is 1)
    --playlist-end NUMBER            Playlist video to end at (default is last)
    --playlist-items ITEM_SPEC       Playlist video items to download. Specify
                                     indices of the videos in the playlist
                                     separated by commas like: "--playlist-items
                                     1,2,5,8" if you want to download videos
                                     indexed 1, 2, 5, 8 in the playlist. You can
                                     specify range: "--playlist-items
                                     1-3,7,10-13", it will download the videos
                                     at index 1, 2, 3, 7, 10, 11, 12 and 13
    --min-filesize SIZE              Do not download any videos smaller than
                                     SIZE (e.g. 50k or 44.6m)
    --max-filesize SIZE              Do not download any videos larger than SIZE
                                     (e.g. 50k or 44.6m)
    --date DATE                      Download only videos uploaded on this date.
                                     The date can be "YYYYMMDD" or in the format
                                     "(now|today)[+-][0-9](day|week|month|year)(
                                     s)?"
    --datebefore DATE                Download only videos uploaded on or before
                                     this date. The date formats accepted is the
                                     same as --date
    --dateafter DATE                 Download only videos uploaded on or after
                                     this date. The date formats accepted is the
                                     same as --date
    --match-filter FILTER            Generic video filter. Any field (see
                                     "OUTPUT TEMPLATE") can be compared with a
                                     number or a string using the operators
                                     defined in "Filtering formats". You can
                                     also simply specify a field to match if the
                                     field is present and "!field" to check if
                                     the field is not present. In addition,
                                     Python style regular expression matching
                                     can be done using "~=", and multiple
                                     filters can be checked with "&". Use a "\"
                                     to escape "&" or quotes if needed. Eg:
                                     --match-filter "!is_live & like_count>?100
                                     & description~='(?i)\bcats \& dogs\b'"
                                     matches only videos that are not live, has
                                     a like count more than 100 (or the like
                                     field is not available), and also has a
                                     description that contains the phrase "cats
                                     & dogs" (ignoring case)
    --no-match-filter                Do not use generic video filter (default)
    --no-playlist                    Download only the video, if the URL refers
                                     to a video and a playlist
    --yes-playlist                   Download the playlist, if the URL refers to
                                     a video and a playlist
    --age-limit YEARS                Download only videos suitable for the given
                                     age
    --download-archive FILE          Download only videos not listed in the
                                     archive file. Record the IDs of all
                                     downloaded videos in it
    --no-download-archive            Do not use archive file (default)
    --max-downloads NUMBER           Abort after downloading NUMBER files
    --break-on-existing              Stop the download process when encountering
                                     a file that is in the archive
    --break-on-reject                Stop the download process when encountering
                                     a file that has been filtered out
    --break-per-input                Make --break-on-existing and --break-on-
                                     reject act only on the current input URL
    --no-break-per-input             --break-on-existing and --break-on-reject
                                     terminates the entire download queue
    --skip-playlist-after-errors N   Number of allowed failures until the rest
                                     of the playlist is skipped

## Download Options:
    -N, --concurrent-fragments N     Number of fragments of a dash/hlsnative
                                     video that should be download concurrently
                                     (default is 1)
    -r, --limit-rate RATE            Maximum download rate in bytes per second
                                     (e.g. 50K or 4.2M)
    --throttled-rate RATE            Minimum download rate in bytes per second
                                     below which throttling is assumed and the
                                     video data is re-extracted (e.g. 100K)
    -R, --retries RETRIES            Number of retries (default is 10), or
                                     "infinite"
    --fragment-retries RETRIES       Number of retries for a fragment (default
                                     is 10), or "infinite" (DASH, hlsnative and
                                     ISM)
    --skip-unavailable-fragments     Skip unavailable fragments for DASH,
                                     hlsnative and ISM (default) (Alias: --no-
                                     abort-on-unavailable-fragment)
    --abort-on-unavailable-fragment  Abort downloading if a fragment is
                                     unavailable (Alias: --no-skip-unavailable-
                                     fragments)
    --keep-fragments                 Keep downloaded fragments on disk after
                                     downloading is finished
    --no-keep-fragments              Delete downloaded fragments after
                                     downloading is finished (default)
    --buffer-size SIZE               Size of download buffer (e.g. 1024 or 16K)
                                     (default is 1024)
    --resize-buffer                  The buffer size is automatically resized
                                     from an initial value of --buffer-size
                                     (default)
    --no-resize-buffer               Do not automatically adjust the buffer size
    --http-chunk-size SIZE           Size of a chunk for chunk-based HTTP
                                     downloading (e.g. 10485760 or 10M) (default
                                     is disabled). May be useful for bypassing
                                     bandwidth throttling imposed by a webserver
                                     (experimental)
    --playlist-reverse               Download playlist videos in reverse order
    --no-playlist-reverse            Download playlist videos in default order
                                     (default)
    --playlist-random                Download playlist videos in random order
    --xattr-set-filesize             Set file xattribute ytdl.filesize with
                                     expected file size
    --hls-use-mpegts                 Use the mpegts container for HLS videos;
                                     allowing some players to play the video
                                     while downloading, and reducing the chance
                                     of file corruption if download is
                                     interrupted. This is enabled by default for
                                     live streams
    --no-hls-use-mpegts              Do not use the mpegts container for HLS
                                     videos. This is default when not
                                     downloading live streams
    --downloader [PROTO:]NAME        Name or path of the external downloader to
                                     use (optionally) prefixed by the protocols
                                     (http, ftp, m3u8, dash, rstp, rtmp, mms) to
                                     use it for. Currently supports native,
                                     aria2c, avconv, axel, curl, ffmpeg, httpie,
                                     wget (Recommended: aria2c). You can use
                                     this option multiple times to set different
                                     downloaders for different protocols. For
                                     example, --downloader aria2c --downloader
                                     "dash,m3u8:native" will use aria2c for
                                     http/ftp downloads, and the native
                                     downloader for dash/m3u8 downloads (Alias:
                                     --external-downloader)
    --downloader-args NAME:ARGS      Give these arguments to the external
                                     downloader. Specify the downloader name and
                                     the arguments separated by a colon ":". For
                                     ffmpeg, arguments can be passed to
                                     different positions using the same syntax
                                     as --postprocessor-args. You can use this
                                     option multiple times to give different
                                     arguments to different downloaders
                                     (Alias: --external-downloader-args)

## Filesystem Options:
    -a, --batch-file FILE            File containing URLs to download ('-' for
                                     stdin), one URL per line. Lines starting
                                     with '#', ';' or ']' are considered as
                                     comments and ignored
    --no-batch-file                  Do not read URLs from batch file (default)
    -P, --paths [TYPES:]PATH         The paths where the files should be
                                     downloaded. Specify the type of file and
                                     the path separated by a colon ":". All the
                                     same types as --output are supported.
                                     Additionally, you can also provide "home"
                                     (default) and "temp" paths. All
                                     intermediary files are first downloaded to
                                     the temp path and then the final files are
                                     moved over to the home path after download
                                     is finished. This option is ignored if
                                     --output is an absolute path
    -o, --output [TYPES:]TEMPLATE    Output filename template; see "OUTPUT
                                     TEMPLATE" for details
    --output-na-placeholder TEXT     Placeholder value for unavailable meta
                                     fields in output filename template
                                     (default: "NA")
    --restrict-filenames             Restrict filenames to only ASCII
                                     characters, and avoid "&" and spaces in
                                     filenames
    --no-restrict-filenames          Allow Unicode characters, "&" and spaces in
                                     filenames (default)
    --windows-filenames              Force filenames to be Windows-compatible
    --no-windows-filenames           Make filenames Windows-compatible only if
                                     using Windows (default)
    --trim-filenames LENGTH          Limit the filename length (excluding
                                     extension) to the specified number of
                                     characters
    -w, --no-overwrites              Do not overwrite any files
    --force-overwrites               Overwrite all video and metadata files.
                                     This option includes --no-continue
    --no-force-overwrites            Do not overwrite the video, but overwrite
                                     related files (default)
    -c, --continue                   Resume partially downloaded files/fragments
                                     (default)
    --no-continue                    Do not resume partially downloaded
                                     fragments. If the file is not fragmented,
                                     restart download of the entire file
    --part                           Use .part files instead of writing directly
                                     into output file (default)
    --no-part                        Do not use .part files - write directly
                                     into output file
    --mtime                          Use the Last-modified header to set the
                                     file modification time (default)
    --no-mtime                       Do not use the Last-modified header to set
                                     the file modification time
    --write-description              Write video description to a .description
                                     file
    --no-write-description           Do not write video description (default)
    --write-info-json                Write video metadata to a .info.json file
                                     (this may contain personal information)
    --no-write-info-json             Do not write video metadata (default)
    --write-playlist-metafiles       Write playlist metadata in addition to the
                                     video metadata when using --write-info-
                                     json, --write-description etc. (default)
    --no-write-playlist-metafiles    Do not write playlist metadata when using
                                     --write-info-json, --write-description etc.
    --clean-infojson                 Remove some private fields such as
                                     filenames from the infojson. Note that it
                                     could still contain some personal
                                     information (default)
    --no-clean-infojson              Write all fields to the infojson
    --write-comments                 Retrieve video comments to be placed in the
                                     infojson. The comments are fetched even
                                     without this option if the extraction is
                                     known to be quick (Alias: --get-comments)
    --no-write-comments              Do not retrieve video comments unless the
                                     extraction is known to be quick (Alias:
                                     --no-get-comments)
    --load-info-json FILE            JSON file containing the video information
                                     (created with the "--write-info-json"
                                     option)
    --cookies FILE                   Netscape formatted file to read cookies
                                     from and dump cookie jar in
    --no-cookies                     Do not read/dump cookies from/to file
                                     (default)
    --cookies-from-browser BROWSER[:PROFILE]
                                     Load cookies from a user profile of the
                                     given web browser. Currently supported
                                     browsers are: brave, chrome, chromium,
                                     edge, firefox, opera, safari, vivaldi. You
                                     can specify the user profile name or
                                     directory using "BROWSER:PROFILE_NAME" or
                                     "BROWSER:PROFILE_PATH". If no profile is
                                     given, the most recently accessed one is
                                     used
    --no-cookies-from-browser        Do not load cookies from browser (default)
    --cache-dir DIR                  Location in the filesystem where youtube-dl
                                     can store some downloaded information (such
                                     as client ids and signatures) permanently.
                                     By default $XDG_CACHE_HOME/yt-dlp or
                                     ~/.cache/yt-dlp
    --no-cache-dir                   Disable filesystem caching
    --rm-cache-dir                   Delete all filesystem cache files
    --rm-long-name-dir               Deletes all filename-splitting-related
                                     empty directories in working directory

## Thumbnail Options:
    --write-thumbnail                Write thumbnail image to disk
    --no-write-thumbnail             Do not write thumbnail image to disk
                                     (default)
    --write-all-thumbnails           Write all thumbnail image formats to disk
    --list-thumbnails                List available thumbnails of each video.
                                     Simulate unless --no-simulate is used

## Internet Shortcut Options:
    --write-link                     Write an internet shortcut file, depending
                                     on the current platform (.url, .webloc or
                                     .desktop). The URL may be cached by the OS
    --write-url-link                 Write a .url Windows internet shortcut. The
                                     OS caches the URL based on the file path
    --write-webloc-link              Write a .webloc macOS internet shortcut
    --write-desktop-link             Write a .desktop Linux internet shortcut

## Verbosity and Simulation Options:
    -q, --quiet                      Activate quiet mode. If used with
                                     --verbose, print the log to stderr
    --no-warnings                    Ignore warnings
    -s, --simulate                   Do not download the video and do not write
                                     anything to disk
    --no-simulate                    Download the video even if printing/listing
                                     options are used
    --ignore-no-formats-error        Ignore "No video formats" error. Useful for
                                     extracting metadata even if the videos are
                                     not actually available for download
                                     (experimental)
    --no-ignore-no-formats-error     Throw error when no downloadable video
                                     formats are found (default)
    --skip-download                  Do not download the video but write all
                                     related files (Alias: --no-download)
    -O, --print TEMPLATE             Quiet, but print the given fields for each
                                     video. Simulate unless --no-simulate is
                                     used. Either a field name or same syntax as
                                     the output template can be used
    -j, --dump-json                  Quiet, but print JSON information for each
                                     video. Simulate unless --no-simulate is
                                     used. See "OUTPUT TEMPLATE" for a
                                     description of available keys
    -J, --dump-single-json           Quiet, but print JSON information for each
                                     url or infojson passed. Simulate unless
                                     --no-simulate is used. If the URL refers to
                                     a playlist, the whole playlist information
                                     is dumped in a single line
    --force-write-archive            Force download archive entries to be
                                     written as far as no errors occur, even if
                                     -s or another simulation option is used
                                     (Alias: --force-download-archive)
    --newline                        Output progress bar as new lines
    --no-progress                    Do not print progress bar
    --progress                       Show progress bar, even if in quiet mode
    --console-title                  Display progress in console titlebar
    --progress-template [TYPES:]TEMPLATE
                                     Template for progress outputs, optionally
                                     prefixed with one of "download:" (default),
                                     "download-title:" (the console title),
                                     "postprocess:",  or "postprocess-title:".
                                     The video's fields are accessible under the
                                     "info" key and the progress attributes are
                                     accessible under "progress" key. E.g.:
                                     --console-title --progress-template
                                     "download-title:%(info.id)s-%(progress.eta)s"
    -v, --verbose                    Print various debugging information
    --dump-pages                     Print downloaded pages encoded using base64
                                     to debug problems (very verbose)
    --write-pages                    Write downloaded intermediary pages to
                                     files in the current directory to debug
                                     problems
    --print-traffic                  Display sent and read HTTP traffic

## Workarounds:
    --encoding ENCODING              Force the specified encoding (experimental)
    --no-check-certificates          Suppress HTTPS certificate validation
    --prefer-insecure                Use an unencrypted connection to retrieve
                                     information about the video (Currently
                                     supported only for YouTube)
    --user-agent UA                  Specify a custom user agent
    --referer URL                    Specify a custom referer, use if the video
                                     access is restricted to one domain
    --add-header FIELD:VALUE         Specify a custom HTTP header and its value,
                                     separated by a colon ":". You can use this
                                     option multiple times
    --bidi-workaround                Work around terminals that lack
                                     bidirectional text support. Requires bidiv
                                     or fribidi executable in PATH
    --sleep-requests SECONDS         Number of seconds to sleep between requests
                                     during data extraction
    --sleep-interval SECONDS         Number of seconds to sleep before each
                                     download. This is the minimum time to sleep
                                     when used along with --max-sleep-interval
                                     (Alias: --min-sleep-interval)
    --max-sleep-interval SECONDS     Maximum number of seconds to sleep. Can
                                     only be used along with --min-sleep-
                                     interval
    --sleep-subtitles SECONDS        Number of seconds to sleep before each
                                     subtitle download
    --escape-long-names              Split filename longer than 255 bytes into
                                     few path segments. This may create dumb
                                     directories.

## Video Format Options:
    -f, --format FORMAT              Video format code, see "FORMAT SELECTION"
                                     for more details
    -S, --format-sort SORTORDER      Sort the formats by the fields given, see
                                     "Sorting Formats" for more details
    --format-sort-force              Force user specified sort order to have
                                     precedence over all fields, see "Sorting
                                     Formats" for more details
    --no-format-sort-force           Some fields have precedence over the user
                                     specified sort order (default), see
                                     "Sorting Formats" for more details
    --video-multistreams             Allow multiple video streams to be merged
                                     into a single file
    --no-video-multistreams          Only one video stream is downloaded for
                                     each output file (default)
    --audio-multistreams             Allow multiple audio streams to be merged
                                     into a single file
    --no-audio-multistreams          Only one audio stream is downloaded for
                                     each output file (default)
    --prefer-free-formats            Prefer video formats with free containers
                                     over non-free ones of same quality. Use
                                     with "-S ext" to strictly prefer free
                                     containers irrespective of quality
    --no-prefer-free-formats         Don't give any special preference to free
                                     containers (default)
    --check-formats                  Check that the selected formats are
                                     actually downloadable
    --check-all-formats              Check all formats for whether they are
                                     actually downloadable
    --no-check-formats               Do not check that the formats are actually
                                     downloadable
    -F, --list-formats               List available formats of each video.
                                     Simulate unless --no-simulate is used
    --merge-output-format FORMAT     If a merge is required (e.g.
                                     bestvideo+bestaudio), output to given
                                     container format. One of mkv, mp4, ogg,
                                     webm, flv. Ignored if no merge is required
    --live-download-mkv              Changes video file format to MKV when
                                     downloading a live. This is useful if the
                                     computer might shutdown while downloading.

## Subtitle Options:
    --write-subs                     Write subtitle file
    --no-write-subs                  Do not write subtitle file (default)
    --write-auto-subs                Write automatically generated subtitle file
                                     (Alias: --write-automatic-subs)
    --no-write-auto-subs             Do not write auto-generated subtitles
                                     (default) (Alias: --no-write-automatic-subs)
    --list-subs                      List available subtitles of each video.
                                     Simulate unless --no-simulate is used
    --sub-format FORMAT              Subtitle format, accepts formats
                                     preference, for example: "srt" or
                                     "ass/srt/best"
    --sub-langs LANGS                Languages of the subtitles to download (can
                                     be regex) or "all" separated by commas.
                                     (Eg: --sub-langs "en.*,ja") You can prefix
                                     the language code with a "-" to exempt it
                                     from the requested languages. (Eg: --sub-
                                     langs all,-live_chat) Use --list-subs for a
                                     list of available language tags

## Authentication Options:
    -u, --username USERNAME          Login with this account ID
    -p, --password PASSWORD          Account password. If this option is left
                                     out, yt-dlp will ask interactively
    -2, --twofactor TWOFACTOR        Two-factor authentication code
    -n, --netrc                      Use .netrc authentication data
    --netrc-location PATH            Location of .netrc authentication data;
                                     either the path or its containing
                                     directory. Defaults to ~/.netrc
    --video-password PASSWORD        Video password (vimeo, youku)
    --ap-mso MSO                     Adobe Pass multiple-system operator (TV
                                     provider) identifier, use --ap-list-mso for
                                     a list of available MSOs
    --ap-username USERNAME           Multiple-system operator account login
    --ap-password PASSWORD           Multiple-system operator account password.
                                     If this option is left out, yt-dlp will ask
                                     interactively
    --ap-list-mso                    List all supported multiple-system
                                     operators

## Post-Processing Options:
    -x, --extract-audio              Convert video files to audio-only files
                                     (requires ffmpeg and ffprobe)
    --audio-format FORMAT            Specify audio format to convert the audio
                                     to when -x is used. Currently supported
                                     formats are: best (default) or one of
                                     best|aac|flac|mp3|m4a|opus|vorbis|wav|alac
    --audio-quality QUALITY          Specify ffmpeg audio quality, insert a
                                     value between 0 (best) and 10 (worst) for
                                     VBR or a specific bitrate like 128K
                                     (default 5)
    --remux-video FORMAT             Remux the video into another container if
                                     necessary (currently supported: mp4|mkv|flv
                                     |webm|mov|avi|mp3|mka|m4a|ogg|opus). If
                                     target container does not support the
                                     video/audio codec, remuxing will fail. You
                                     can specify multiple rules; Eg.
                                     "aac>m4a/mov>mp4/mkv" will remux aac to
                                     m4a, mov to mp4 and anything else to mkv.
    --recode-video FORMAT            Re-encode the video into another format if
                                     re-encoding is necessary. The syntax and
                                     supported formats are the same as --remux-video
    --postprocessor-args NAME:ARGS   Give these arguments to the postprocessors.
                                     Specify the postprocessor/executable name
                                     and the arguments separated by a colon ":"
                                     to give the argument to the specified
                                     postprocessor/executable. Supported PP are:
                                     Merger, ModifyChapters, SplitChapters,
                                     ExtractAudio, VideoRemuxer, VideoConvertor,
                                     Metadata, EmbedSubtitle, EmbedThumbnail,
                                     SubtitlesConvertor, ThumbnailsConvertor,
                                     FixupStretched, FixupM4a, FixupM3u8,
                                     FixupTimestamp and FixupDuration. The
                                     supported executables are: AtomicParsley,
                                     FFmpeg and FFprobe. You can also specify
                                     "PP+EXE:ARGS" to give the arguments to the
                                     specified executable only when being used
                                     by the specified postprocessor.
                                     Additionally, for ffmpeg/ffprobe, "_i"/"_o"
                                     can be appended to the prefix optionally
                                     followed by a number to pass the argument
                                     before the specified input/output file. Eg:
                                     --ppa "Merger+ffmpeg_i1:-v quiet". You can
                                     use this option multiple times to give
                                     different arguments to different
                                     postprocessors. (Alias: --ppa)
    -k, --keep-video                 Keep the intermediate video file on disk
                                     after post-processing
    --no-keep-video                  Delete the intermediate video file after
                                     post-processing (default)
    --post-overwrites                Overwrite post-processed files (default)
    --no-post-overwrites             Do not overwrite post-processed files
    --embed-subs                     Embed subtitles in the video (only for mp4,
                                     webm and mkv videos)
    --no-embed-subs                  Do not embed subtitles (default)
    --embed-thumbnail                Embed thumbnail in the video as cover art
    --no-embed-thumbnail             Do not embed thumbnail (default)
    --embed-metadata                 Embed metadata to the video file. Also
                                     embeds chapters/infojson if present unless
                                     --no-embed-chapters/--no-embed-info-json
                                     are used (Alias: --add-metadata)
    --no-embed-metadata              Do not add metadata to file (default)
                                     (Alias: --no-add-metadata)
    --embed-chapters                 Add chapter markers to the video file
                                     (Alias: --add-chapters)
    --no-embed-chapters              Do not add chapter markers (default)
                                     (Alias: --no-add-chapters)
    --embed-info-json                Embed the infojson as an attachment to
                                     mkv/mka video files
    --no-embed-info-json             Do not embed the infojson as an attachment
                                     to the video file
    --parse-metadata FROM:TO         Parse additional metadata like title/artist
                                     from other fields; see "MODIFYING METADATA"
                                     for details
    --replace-in-metadata FIELDS REGEX REPLACE
                                     Replace text in a metadata field using the
                                     given regex. This option can be used
                                     multiple times
    --xattrs                         Write metadata to the video file's xattrs
                                     (using dublin core and xdg standards)
    --fixup POLICY                   Automatically correct known faults of the
                                     file. One of never (do nothing), warn (only
                                     emit a warning), detect_or_warn (the
                                     default; fix file if we can, warn
                                     otherwise), force (try fixing even if file
                                     already exists
    --ffmpeg-location PATH           Location of the ffmpeg binary; either the
                                     path to the binary or its containing
                                     directory
    --exec CMD                       Execute a command on the file after
                                     downloading and post-processing. Same
                                     syntax as the output template can be used
                                     to pass any field as arguments to the
                                     command. An additional field "filepath"
                                     that contains the final path of the
                                     downloaded file is also available. If no
                                     fields are passed, %(filepath)q is appended
                                     to the end of the command. This option can
                                     be used multiple times
    --no-exec                        Remove any previously defined --exec
    --exec-before-download CMD       Execute a command before the actual
                                     download. The syntax is the same as --exec
                                     but "filepath" is not available. This
                                     option can be used multiple times
    --no-exec-before-download        Remove any previously defined
                                     --exec-before-download
    --convert-subs FORMAT            Convert the subtitles to another format
                                     (currently supported: srt|vtt|ass|lrc)
                                     (Alias: --convert-subtitles)
    --convert-thumbnails FORMAT      Convert the thumbnails to another format
                                     (currently supported: jpg|png)
    --split-chapters                 Split video into multiple files based on
                                     internal chapters. The "chapter:" prefix
                                     can be used with "--paths" and "--output"
                                     to set the output filename for the split
                                     files. See "OUTPUT TEMPLATE" for details
    --no-split-chapters              Do not split video based on chapters
                                     (default)
    --remove-chapters REGEX          Remove chapters whose title matches the
                                     given regular expression. Time ranges
                                     prefixed by a "*" can also be used in place
                                     of chapters to remove the specified range.
                                     Eg: --remove-chapters "*10:15-15:00"
                                     --remove-chapters "intro". This option can
                                     be used multiple times
    --no-remove-chapters             Do not remove any chapters from the file
                                     (default)
    --force-keyframes-at-cuts        Force keyframes around the chapters before
                                     removing/splitting them. Requires a
                                     reencode and thus is very slow, but the
                                     resulting video may have fewer artifacts
                                     around the cuts
    --no-force-keyframes-at-cuts     Do not force keyframes around the chapters
                                     when cutting/splitting (default)
    --use-postprocessor NAME[:ARGS]  The (case sensitive) name of plugin
                                     postprocessors to be enabled, and
                                     (optionally) arguments to be passed to it,
                                     seperated by a colon ":". ARGS are a
                                     semicolon ";" delimited list of NAME=VALUE.
                                     The "when" argument determines when the
                                     postprocessor is invoked. It can be one of
                                     "pre_process" (after extraction),
                                     "before_dl" (before video download),
                                     "post_process" (after video download;
                                     default) or "after_move" (after moving file
                                     to their final locations). This option can
                                     be used multiple times to add different
                                     postprocessors

## SponsorBlock Options:
Make chapter entries for, or remove various segments (sponsor,
    introductions, etc.) from downloaded YouTube videos using the
    [SponsorBlock API](https://sponsor.ajay.app)

    --sponsorblock-mark CATS         SponsorBlock categories to create chapters
                                     for, separated by commas. Available
                                     categories are all, default(=all), sponsor,
                                     intro, outro, selfpromo, preview, filler,
                                     interaction, music_offtopic, poi_highlight.
                                     You can prefix the category with a "-" to
                                     exempt it. See [1] for description of the
                                     categories. Eg: --sponsorblock-mark all,-preview
                                     [1] https://wiki.sponsor.ajay.app/w/Segment_Categories
    --sponsorblock-remove CATS       SponsorBlock categories to be removed from
                                     the video file, separated by commas. If a
                                     category is present in both mark and
                                     remove, remove takes precedence. The syntax
                                     and available categories are the same as
                                     for --sponsorblock-mark except that
                                     "default" refers to "all,-filler" and
                                     poi_highlight is not available
    --sponsorblock-chapter-title TEMPLATE
                                     The title template for SponsorBlock
                                     chapters created by --sponsorblock-mark.
                                     The same syntax as the output template is
                                     used, but the only available fields are
                                     start_time, end_time, category, categories,
                                     name, category_names. Defaults to
                                     "[SponsorBlock]: %(category_names)l"
    --no-sponsorblock                Disable both --sponsorblock-mark and
                                     --sponsorblock-remove
    --sponsorblock-api URL           SponsorBlock API location, defaults to
                                     https://sponsor.ajay.app

## Extractor Options:
    --extractor-retries RETRIES      Number of retries for known extractor
                                     errors (default is 3), or "infinite"
    --allow-dynamic-mpd              Process dynamic DASH manifests (default)
                                     (Alias: --no-ignore-dynamic-mpd)
    --ignore-dynamic-mpd             Do not process dynamic DASH manifests
                                     (Alias: --no-allow-dynamic-mpd)
    --hls-split-discontinuity        Split HLS playlists to different formats at
                                     discontinuities such as ad breaks
    --no-hls-split-discontinuity     Do not split HLS playlists to different
                                     formats at discontinuities such as ad
                                     breaks (default)
    --extractor-args KEY:ARGS        Pass these arguments to the extractor. See
                                     "EXTRACTOR ARGUMENTS" for details. You can
                                     use this option multiple times to give
                                     arguments for different extractors

# CONFIGURATION

You can configure yt-dlp by placing any supported command line option to a configuration file. The configuration is loaded from the following locations:

1. **Main Configuration**: The file given by `--config-location`
1. **Portable Configuration**: `yt-dlp.conf` in the same directory as the bundled binary. If you are running from source-code (`<root dir>/yt_dlp/__main__.py`), the root directory is used instead.
1. **Home Configuration**: `yt-dlp.conf` in the home path given by `-P "home:<path>"`, or in the current directory if no such path is given
1. **User Configuration**:
    * `%XDG_CONFIG_HOME%/yt-dlp/config` (recommended on Linux/macOS)
    * `%XDG_CONFIG_HOME%/yt-dlp.conf`
    * `%APPDATA%/yt-dlp/config` (recommended on Windows)
    * `%APPDATA%/yt-dlp/config.txt`
    * `~/yt-dlp.conf`
    * `~/yt-dlp.conf.txt`

    `%XDG_CONFIG_HOME%` defaults to `~/.config` if undefined. On windows, `%APPDATA%` generally points to (`C:\Users\<user name>\AppData\Roaming`) and `~` points to `%HOME%` if present, `%USERPROFILE%` (generally `C:\Users\<user name>`), or `%HOMEDRIVE%%HOMEPATH%`
1. **System Configuration**: `/etc/yt-dlp.conf`

For example, with the following configuration file yt-dlp will always extract the audio, not copy the mtime, use a proxy and save all videos under `YouTube` directory in your home directory:
```
# Lines starting with # are comments

# Always extract audio
-x

# Do not copy the mtime
--no-mtime

# Use this proxy
--proxy 127.0.0.1:3128

# Save all videos under YouTube directory in your home directory
-o ~/YouTube/%(title)s.%(ext)s
```

Note that options in configuration file are just the same options aka switches used in regular command line calls; thus there **must be no whitespace** after `-` or `--`, e.g. `-o` or `--proxy` but not `- o` or `-- proxy`.

You can use `--ignore-config` if you want to disable all configuration files for a particular yt-dlp run. If `--ignore-config` is found inside any configuration file, no further configuration will be loaded. For example, having the option in the portable configuration file prevents loading of home, user, and system configurations. Additionally, (for backward compatibility) if `--ignore-config` is found inside the system configuration file, the user configuration is not loaded.

### Authentication with `.netrc` file

You may also want to configure automatic credentials storage for extractors that support authentication (by providing login and password with `--username` and `--password`) in order not to pass credentials as command line arguments on every yt-dlp execution and prevent tracking plain text passwords in the shell command history. You can achieve this using a [`.netrc` file](https://stackoverflow.com/tags/.netrc/info) on a per extractor basis. For that you will need to create a `.netrc` file in `--netrc-location` and restrict permissions to read/write by only you:
```
touch $HOME/.netrc
chmod a-rwx,u+rw $HOME/.netrc
```
After that you can add credentials for an extractor in the following format, where *extractor* is the name of the extractor in lowercase:
```
machine <extractor> login <username> password <password>
```
For example:
```
machine youtube login myaccount@gmail.com password my_youtube_password
machine twitch login my_twitch_account_name password my_twitch_password
```
To activate authentication with the `.netrc` file you should pass `--netrc` to yt-dlp or place it in the [configuration file](#configuration).

The default location of the .netrc file is `$HOME` (`~`) in UNIX. On Windows, it is `%HOME%` if present, `%USERPROFILE%` (generally `C:\Users\<user name>`) or `%HOMEDRIVE%%HOMEPATH%`

# OUTPUT TEMPLATE

The `-o` option is used to indicate a template for the output file names while `-P` option is used to specify the path each type of file should be saved to.

**tl;dr:** [navigate me to examples](#output-template-examples).

The simplest usage of `-o` is not to set any template arguments when downloading a single file, like in `yt-dlp -o funny_video.flv "https://some/video"` (hard-coding file extension like this is _not_ recommended and could break some post-processing).

It may however also contain special sequences that will be replaced when downloading each video. The special sequences may be formatted according to [Python string formatting operations](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting). For example, `%(NAME)s` or `%(NAME)05d`. To clarify, that is a percent symbol followed by a name in parentheses, followed by formatting operations.

The field names themselves (the part inside the parenthesis) can also have some special formatting:
1. **Object traversal**: The dictionaries and lists available in metadata can be traversed by using a `.` (dot) separator. You can also do python slicing using `:`. Eg: `%(tags.0)s`, `%(subtitles.en.-1.ext)s`, `%(id.3:7:-1)s`, `%(formats.:.format_id)s`. `%()s` refers to the entire infodict. Note that all the fields that become available using this method are not listed below. Use `-j` to see such fields
1. **Addition**: Addition and subtraction of numeric fields can be done using `+` and `-` respectively. Eg: `%(playlist_index+10)03d`, `%(n_entries+1-playlist_index)d`
1. **Date/time Formatting**: Date/time fields can be formatted according to [strftime formatting](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) by specifying it separated from the field name using a `>`. Eg: `%(duration>%H-%M-%S)s`, `%(upload_date>%Y-%m-%d)s`, `%(epoch-3600>%H-%M-%S)s`
1. **Alternatives**: Alternate fields can be specified seperated with a `,`. Eg: `%(release_date>%Y,upload_date>%Y|Unknown)s`
1. **Default**: A literal default value can be specified for when the field is empty using a `|` seperator. This overrides `--output-na-template`. Eg: `%(uploader|Unknown)s`
1. **More Conversions**: In addition to the normal format types `diouxXeEfFgGcrs`, `B`, `j`, `l`, `q` can be used for converting to **B**ytes, **j**son (flag `#` for pretty-printing), a comma seperated **l**ist (flag `#` for `\n` newline-seperated) and a string **q**uoted for the terminal (flag `#` to split a list into different arguments), respectively
1. **Unicode normalization**: The format type `U` can be used for NFC [unicode normalization](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize). The alternate form flag (`#`) changes the normalization to NFD and the conversion flag `+` can be used for NFKC/NFKD compatibility equivalence normalization. Eg: `%(title)+.100U` is NFKC

To summarize, the general syntax for a field is:
```
%(name[.keys][addition][>strf][,alternate][|default])[flags][width][.precision][length]type
```

Additionally, you can set different output templates for the various metadata files separately from the general output template by specifying the type of file followed by the template separated by a colon `:`. The different file types supported are `subtitle`, `thumbnail`, `description`, `annotation` (deprecated), `infojson`, `link`, `pl_thumbnail`, `pl_description`, `pl_infojson`, `chapter`. For example, `-o '%(title)s.%(ext)s' -o 'thumbnail:%(title)s\%(title)s.%(ext)s'`  will put the thumbnails in a folder with the same name as the video. If any of the templates (except default) is empty, that type of file will not be written. Eg: `--write-thumbnail -o "thumbnail:"` will write thumbnails only for playlists and not for video.

The available fields are:

 - `id` (string): Video identifier
 - `title` (string): Video title
 - `url` (string): Video URL
 - `ext` (string): Video filename extension
 - `alt_title` (string): A secondary title of the video
 - `description` (string): The description of the video
 - `display_id` (string): An alternative identifier for the video
 - `uploader` (string): Full name of the video uploader
 - `license` (string): License name the video is licensed under
 - `creator` (string): The creator of the video
 - `timestamp` (numeric): UNIX timestamp of the moment the video became available
 - `upload_date` (string): Video upload date (YYYYMMDD)
 - `release_date` (string): The date (YYYYMMDD) when the video was released
 - `release_timestamp` (numeric): UNIX timestamp of the moment the video was released
 - `uploader_id` (string): Nickname or id of the video uploader
 - `channel` (string): Full name of the channel the video is uploaded on
 - `channel_id` (string): Id of the channel
 - `location` (string): Physical location where the video was filmed
 - `duration` (numeric): Length of the video in seconds
 - `duration_string` (string): Length of the video (HH:mm:ss)
 - `view_count` (numeric): How many users have watched the video on the platform
 - `like_count` (numeric): Number of positive ratings of the video
 - `dislike_count` (numeric): Number of negative ratings of the video
 - `repost_count` (numeric): Number of reposts of the video
 - `average_rating` (numeric): Average rating give by users, the scale used depends on the webpage
 - `comment_count` (numeric): Number of comments on the video (For some extractors, comments are only downloaded at the end, and so this field cannot be used)
 - `age_limit` (numeric): Age restriction for the video (years)
 - `live_status` (string): One of 'is_live', 'was_live', 'is_upcoming', 'not_live'
 - `is_live` (boolean): Whether this video is a live stream or a fixed-length video
 - `was_live` (boolean): Whether this video was originally a live stream
 - `playable_in_embed` (string): Whether this video is allowed to play in embedded players on other sites
 - `availability` (string): Whether the video is 'private', 'premium_only', 'subscriber_only', 'needs_auth', 'unlisted' or 'public'
 - `start_time` (numeric): Time in seconds where the reproduction should start, as specified in the URL
 - `end_time` (numeric): Time in seconds where the reproduction should end, as specified in the URL
 - `format` (string): A human-readable description of the format
 - `format_id` (string): Format code specified by `--format`
 - `format_note` (string): Additional info about the format
 - `width` (numeric): Width of the video
 - `height` (numeric): Height of the video
 - `resolution` (string): Textual description of width and height
 - `tbr` (numeric): Average bitrate of audio and video in KBit/s
 - `abr` (numeric): Average audio bitrate in KBit/s
 - `acodec` (string): Name of the audio codec in use
 - `asr` (numeric): Audio sampling rate in Hertz
 - `vbr` (numeric): Average video bitrate in KBit/s
 - `fps` (numeric): Frame rate
 - `dynamic_range` (string): The dynamic range of the video
 - `vcodec` (string): Name of the video codec in use
 - `container` (string): Name of the container format
 - `filesize` (numeric): The number of bytes, if known in advance
 - `filesize_approx` (numeric): An estimate for the number of bytes
 - `protocol` (string): The protocol that will be used for the actual download
 - `extractor` (string): Name of the extractor
 - `extractor_key` (string): Key name of the extractor
 - `epoch` (numeric): Unix epoch when creating the file
 - `autonumber` (numeric): Number that will be increased with each download, starting at `--autonumber-start`
 - `n_entries` (numeric): Total number of extracted items in the playlist
 - `playlist` (string): Name or id of the playlist that contains the video
 - `playlist_index` (numeric): Index of the video in the playlist padded with leading zeros according the final index
 - `playlist_autonumber` (numeric): Position of the video in the playlist download queue padded with leading zeros according to the total length of the playlist
 - `playlist_id` (string): Playlist identifier
 - `playlist_title` (string): Playlist title
 - `playlist_uploader` (string): Full name of the playlist uploader
 - `playlist_uploader_id` (string): Nickname or id of the playlist uploader
 - `webpage_url` (string): A URL to the video webpage which if given to yt-dlp should allow to get the same result again
 - `original_url` (string): The URL given by the user (or same as `webpage_url` for playlist entries)
 - `orig_title` (string): Original video title, when extractor altered the title in any reason
 - `orig_description` (string): The original description of the video, when extractor altered the description in any reason

Available for the video that belongs to some logical chapter or section:

 - `chapter` (string): Name or title of the chapter the video belongs to
 - `chapter_number` (numeric): Number of the chapter the video belongs to
 - `chapter_id` (string): Id of the chapter the video belongs to

Available for the video that is an episode of some series or programme:

 - `series` (string): Title of the series or programme the video episode belongs to
 - `season` (string): Title of the season the video episode belongs to
 - `season_number` (numeric): Number of the season the video episode belongs to
 - `season_id` (string): Id of the season the video episode belongs to
 - `episode` (string): Title of the video episode
 - `episode_number` (numeric): Number of the video episode within a season
 - `episode_id` (string): Id of the video episode

Available for the media that is a track or a part of a music album:

 - `track` (string): Title of the track
 - `track_number` (numeric): Number of the track within an album or a disc
 - `track_id` (string): Id of the track
 - `artist` (string): Artist(s) of the track
 - `genre` (string): Genre(s) of the track
 - `album` (string): Title of the album the track belongs to
 - `album_type` (string): Type of the album
 - `album_artist` (string): List of all artists appeared on the album
 - `disc_number` (numeric): Number of the disc or other physical medium the track belongs to
 - `release_year` (numeric): Year (YYYY) when the album was released

Available for `chapter:` prefix when using `--split-chapters` for videos with internal chapters:

 - `section_title` (string): Title of the chapter
 - `section_number` (numeric): Number of the chapter within the file
 - `section_start` (numeric): Start time of the chapter in seconds
 - `section_end` (numeric): End time of the chapter in seconds

Available only when used in `--print`:

 - `urls` (string): The URLs of all requested formats, one in each line
 - `filename` (string): Name of the video file. Note that the actual filename may be different due to post-processing. Use `--exec echo` to get the name after all postprocessing is complete
 
Available only in `--sponsorblock-chapter-title`:

 - `start_time` (numeric): Start time of the chapter in seconds
 - `end_time` (numeric): End time of the chapter in seconds
 - `categories` (list): The SponsorBlock categories the chapter belongs to
 - `category` (string): The smallest SponsorBlock category the chapter belongs to
 - `category_names` (list): Friendly names of the categories
 - `name` (string): Friendly name of the smallest category

Each aforementioned sequence when referenced in an output template will be replaced by the actual value corresponding to the sequence name. Note that some of the sequences are not guaranteed to be present since they depend on the metadata obtained by a particular extractor. Such sequences will be replaced with placeholder value provided with `--output-na-placeholder` (`NA` by default).

**Tip**: Look at the `-j` output to identify which fields are available for the particular URL

For numeric sequences you can use numeric related formatting, for example, `%(view_count)05d` will result in a string with view count padded with zeros up to 5 characters, like in `00042`.

Output templates can also contain arbitrary hierarchical path, e.g. `-o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'` which will result in downloading each video in a directory corresponding to this path template. Any missing directory will be automatically created for you.

To use percent literals in an output template use `%%`. To output to stdout use `-o -`.

The current default template is `%(title)s [%(id)s].%(ext)s`.

In some cases, you don't want special characters such as 中, spaces, or &, such as when transferring the downloaded filename to a Windows system or the filename through an 8bit-unsafe channel. In these cases, add the `--restrict-filenames` flag to get a shorter title.

#### Output template and Windows batch files

If you are using an output template inside a Windows batch file then you must escape plain percent characters (`%`) by doubling, so that `-o "%(title)s-%(id)s.%(ext)s"` should become `-o "%%(title)s-%%(id)s.%%(ext)s"`. However you should not touch `%`'s that are not plain characters, e.g. environment variables for expansion should stay intact: `-o "C:\%HOMEPATH%\Desktop\%%(title)s.%%(ext)s"`.

#### Output template examples

Note that on Windows you need to use double quotes instead of single.

```bash
$ yt-dlp --get-filename -o 'test video.%(ext)s' BaW_jenozKc
test video.webm    # Literal name with correct extension

$ yt-dlp --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc
youtube-dl test video ''_ä↭𝕐.webm    # All kinds of weird characters

$ yt-dlp --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc --restrict-filenames
youtube-dl_test_video_.webm    # Restricted file name

# Download YouTube playlist videos in separate directory indexed by video order in a playlist
$ yt-dlp -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re

# Download YouTube playlist videos in separate directories according to their uploaded year
$ yt-dlp -o '%(upload_date>%Y)s/%(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re

# Download all playlists of YouTube channel/user keeping each playlist in separate directory:
$ yt-dlp -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/user/TheLinuxFoundation/playlists

# Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
$ yt-dlp -u user -p password -P '~/MyVideos' -o '%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s' https://www.udemy.com/java-tutorial/

# Download entire series season keeping each series and each season in separate directory under C:/MyVideos
$ yt-dlp -P "C:/MyVideos" -o "%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s" https://videomore.ru/kino_v_detalayah/5_sezon/367617

# Stream the video being downloaded to stdout
$ yt-dlp -o - BaW_jenozKc
```

# FORMAT SELECTION

By default, yt-dlp tries to download the best available quality if you **don't** pass any options.
This is generally equivalent to using `-f bestvideo*+bestaudio/best`. However, if multiple audiostreams is enabled (`--audio-multistreams`), the default format changes to `-f bestvideo+bestaudio/best`. Similarly, if ffmpeg is unavailable, or if you use yt-dlp to stream to `stdout` (`-o -`), the default becomes `-f best/bestvideo+bestaudio`.

**Deprecation warning**: Latest versions of yt-dlp can stream multiple formats to the stdout simultaneously using ffmpeg. So, in future versions, the default for this will be set to `-f bv*+ba/b` similar to normal downloads. If you want to preserve the `-f b/bv+ba` setting, it is recommended to explicitly specify it in the configuration options.

The general syntax for format selection is `-f FORMAT` (or `--format FORMAT`) where `FORMAT` is a *selector expression*, i.e. an expression that describes format or formats you would like to download.

**tl;dr:** [navigate me to examples](#format-selection-examples).

The simplest case is requesting a specific format, for example with `-f 22` you can download the format with format code equal to 22. You can get the list of available format codes for particular video using `--list-formats` or `-F`. Note that these format codes are extractor specific.

You can also use a file extension (currently `3gp`, `aac`, `flv`, `m4a`, `mp3`, `mp4`, `ogg`, `wav`, `webm` are supported) to download the best quality format of a particular file extension served as a single file, e.g. `-f webm` will download the best quality format with the `webm` extension served as a single file.

You can also use special names to select particular edge case formats:

 - `all`: Select **all formats** separately
 - `mergeall`: Select and **merge all formats** (Must be used with `--audio-multistreams`, `--video-multistreams` or both)
 - `b*`, `best*`: Select the best quality format that **contains either** a video or an audio
 - `b`, `best`: Select the best quality format that **contains both** video and audio. Equivalent to `best*[vcodec!=none][acodec!=none]`
 - `bv`, `bestvideo`: Select the best quality **video-only** format. Equivalent to `best*[acodec=none]`
 - `bv*`, `bestvideo*`: Select the best quality format that **contains video**. It may also contain audio. Equivalent to `best*[vcodec!=none]`
 - `ba`, `bestaudio`: Select the best quality **audio-only** format. Equivalent to `best*[vcodec=none]`
 - `ba*`, `bestaudio*`: Select the best quality format that **contains audio**. It may also contain video. Equivalent to `best*[acodec!=none]`
 - `w*`, `worst*`: Select the worst quality format that contains either a video or an audio
 - `w`, `worst`: Select the worst quality format that contains both video and audio. Equivalent to `worst*[vcodec!=none][acodec!=none]`
 - `wv`, `worstvideo`: Select the worst quality video-only format. Equivalent to `worst*[acodec=none]`
 - `wv*`, `worstvideo*`: Select the worst quality format that contains video. It may also contain audio. Equivalent to `worst*[vcodec!=none]`
 - `wa`, `worstaudio`: Select the worst quality audio-only format. Equivalent to `worst*[vcodec=none]`
 - `wa*`, `worstaudio*`: Select the worst quality format that contains audio. It may also contain video. Equivalent to `worst*[acodec!=none]`

For example, to download the worst quality video-only format you can use `-f worstvideo`. It is however recommended not to use `worst` and related options. When your format selector is `worst`, the format which is worst in all respects is selected. Most of the time, what you actually want is the video with the smallest filesize instead. So it is generally better to use `-f best -S +size,+br,+res,+fps` instead of `-f worst`. See [sorting formats](#sorting-formats) for more details.

You can select the n'th best format of a type by using `best<type>.<n>`. For example, `best.2` will select the 2nd best combined format. Similarly, `bv*.3` will select the 3rd best format that contains a video stream.

If you want to download multiple videos and they don't have the same formats available, you can specify the order of preference using slashes. Note that formats on the left hand side are preferred, for example `-f 22/17/18` will download format 22 if it's available, otherwise it will download format 17 if it's available, otherwise it will download format 18 if it's available, otherwise it will complain that no suitable formats are available for download.

If you want to download several formats of the same video use a comma as a separator, e.g. `-f 22,17,18` will download all these three formats, of course if they are available. Or a more sophisticated example combined with the precedence feature: `-f 136/137/mp4/bestvideo,140/m4a/bestaudio`.

You can merge the video and audio of multiple formats into a single file using `-f <format1>+<format2>+...` (requires ffmpeg installed), for example `-f bestvideo+bestaudio` will download the best video-only format, the best audio-only format and mux them together with ffmpeg.

**Deprecation warning**: Since the *below* described behavior is complex and counter-intuitive, this will be removed and multistreams will be enabled by default in the future. A new operator will be instead added to limit formats to single audio/video

Unless `--video-multistreams` is used, all formats with a video stream except the first one are ignored. Similarly, unless `--audio-multistreams` is used, all formats with an audio stream except the first one are ignored. For example, `-f bestvideo+best+bestaudio --video-multistreams --audio-multistreams` will download and merge all 3 given formats. The resulting file will have 2 video streams and 2 audio streams. But `-f bestvideo+best+bestaudio --no-video-multistreams` will download and merge only `bestvideo` and `bestaudio`. `best` is ignored since another format containing a video stream (`bestvideo`) has already been selected. The order of the formats is therefore important. `-f best+bestaudio --no-audio-multistreams` will download and merge both formats while `-f bestaudio+best --no-audio-multistreams` will ignore `best` and download only `bestaudio`.

## Filtering Formats

You can also filter the video formats by putting a condition in brackets, as in `-f "best[height=720]"` (or `-f "[filesize>10M]"`).

The following numeric meta fields can be used with comparisons `<`, `<=`, `>`, `>=`, `=` (equals), `!=` (not equals):

 - `filesize`: The number of bytes, if known in advance
 - `width`: Width of the video, if known
 - `height`: Height of the video, if known
 - `tbr`: Average bitrate of audio and video in KBit/s
 - `abr`: Average audio bitrate in KBit/s
 - `vbr`: Average video bitrate in KBit/s
 - `asr`: Audio sampling rate in Hertz
 - `fps`: Frame rate

Also filtering work for comparisons `=` (equals), `^=` (starts with), `$=` (ends with), `*=` (contains) and following string meta fields:

 - `ext`: File extension
 - `acodec`: Name of the audio codec in use
 - `vcodec`: Name of the video codec in use
 - `container`: Name of the container format
 - `protocol`: The protocol that will be used for the actual download, lower-case (`http`, `https`, `rtsp`, `rtmp`, `rtmpe`, `mms`, `f4m`, `ism`, `http_dash_segments`, `m3u8`, or `m3u8_native`)
 - `format_id`: A short description of the format
 - `language`: Language code

Any string comparison may be prefixed with negation `!` in order to produce an opposite comparison, e.g. `!*=` (does not contain).

Note that none of the aforementioned meta fields are guaranteed to be present since this solely depends on the metadata obtained by particular extractor, i.e. the metadata offered by the website. Any other field made available by the extractor can also be used for filtering.

Formats for which the value is not known are excluded unless you put a question mark (`?`) after the operator. You can combine format filters, so `-f "[height<=?720][tbr>500]"` selects up to 720p videos (or videos where the height is not known) with a bitrate of at least 500 KBit/s. You can also use the filters with `all` to download all formats that satisfy the filter. For example, `-f "all[vcodec=none]"` selects all audio-only formats.

Format selectors can also be grouped using parentheses, for example if you want to download the best mp4 and webm formats with a height lower than 480 you can use `-f '(mp4,webm)[height<480]'`.

## Sorting Formats

You can change the criteria for being considered the `best` by using `-S` (`--format-sort`). The general format for this is `--format-sort field1,field2...`.

The available fields are:

 - `hasvid`: Gives priority to formats that has a video stream
 - `hasaud`: Gives priority to formats that has a audio stream
 - `ie_pref`: The format preference as given by the extractor
 - `lang`: Language preference as given by the extractor
 - `quality`: The quality of the format as given by the extractor
 - `source`: Preference of the source as given by the extractor
 - `proto`: Protocol used for download (`m3u8_native` > `m3u8` > `https`/`ftps` > `http`/`ftp` > `http_dash_segments` > `websocket_frag` > other > `mms`/`rtsp` > unknown > `f4f`/`f4m`)
 - `vcodec`: Video Codec (`av01` > `vp9.2` > `vp9` > `h265` > `h264` > `vp8` > `h263` > `theora` > other > unknown)
 - `acodec`: Audio Codec (`opus` > `vorbis` > `aac` > `mp4a` > `mp3` > `eac3` > `ac3` > `dts` > other > unknown)
 - `codec`: Equivalent to `vcodec,acodec`
 - `vext`: Video Extension (`mp4` > `webm` > `flv` > other > unknown). If `--prefer-free-formats` is used, `webm` is prefered.
 - `aext`: Audio Extension (`m4a` > `aac` > `mp3` > `ogg` > `opus` > `webm` > other > unknown). If `--prefer-free-formats` is used, the order changes to `opus` > `ogg` > `webm` > `m4a` > `mp3` > `aac`.
 - `ext`: Equivalent to `vext,aext`
 - `filesize`: Exact filesize, if known in advance
 - `fs_approx`: Approximate filesize calculated from the manifests
 - `size`: Exact filesize if available, otherwise approximate filesize
 - `height`: Height of video
 - `width`: Width of video
 - `res`: Video resolution, calculated as the smallest dimension.
 - `fps`: Framerate of video
 - `hdr`: The dynamic range of the video (`DV` > `HDR12` > `HDR10+` > `HDR10` > `SDR`)
 - `tbr`: Total average bitrate in KBit/s
 - `vbr`: Average video bitrate in KBit/s
 - `abr`: Average audio bitrate in KBit/s
 - `br`: Equivalent to using `tbr,vbr,abr`
 - `asr`: Audio sample rate in Hz
 
**Deprecation warning**: Many of these fields have (currently undocumented) aliases, that may be removed in a future version. It is recommended to use only the documented field names.

All fields, unless specified otherwise, are sorted in descending order. To reverse this, prefix the field with a `+`. Eg: `+res` prefers format with the smallest resolution. Additionally, you can suffix a preferred value for the fields, separated by a `:`. Eg: `res:720` prefers larger videos, but no larger than 720p and the smallest video if there are no videos less than 720p. For `codec` and `ext`, you can provide two preferred values, the first for video and the second for audio. Eg: `+codec:avc:m4a` (equivalent to `+vcodec:avc,+acodec:m4a`) sets the video codec preference to `h264` > `h265` > `vp9` > `vp9.2` > `av01` > `vp8` > `h263` > `theora` and audio codec preference to `mp4a` > `aac` > `vorbis` > `opus` > `mp3` > `ac3` > `dts`. You can also make the sorting prefer the nearest values to the provided by using `~` as the delimiter. Eg: `filesize~1G` prefers the format with filesize closest to 1 GiB.

The fields `hasvid` and `ie_pref` are always given highest priority in sorting, irrespective of the user-defined order. This behaviour can be changed by using `--format-sort-force`. Apart from these, the default order used is: `lang,quality,res,fps,hdr:12,codec:vp9.2,size,br,asr,proto,ext,hasaud,source,id`. The extractors may override this default order, but they cannot override the user-provided order.

Note that the default has `codec:vp9.2`; i.e. `av1` is not prefered. Similarly, the default for hdr is `hdr:12`; i.e. dolby vision is not prefered. These choices are made since DV and AV1 formats are not yet fully compatible with most devices. This may be changed in the future as more devices become capable of smoothly playing back these formats.

If your format selector is `worst`, the last item is selected after sorting. This means it will select the format that is worst in all respects. Most of the time, what you actually want is the video with the smallest filesize instead. So it is generally better to use `-f best -S +size,+br,+res,+fps`.

**Tip**: You can use the `-v -F` to see how the formats have been sorted (worst to best).

## Format Selection examples

Note that on Windows you may need to use double quotes instead of single.

```bash
# Download and merge the best video-only format and the best audio-only format,
# or download the best combined format if video-only format is not available
$ yt-dlp -f 'bv+ba/b'

# Download best format that contains video,
# and if it doesn't already have an audio stream, merge it with best audio-only format
$ yt-dlp -f 'bv*+ba/b'

# Same as above
$ yt-dlp

# Download the best video-only format and the best audio-only format without merging them
# For this case, an output template should be used since
# by default, bestvideo and bestaudio will have the same file name.
$ yt-dlp -f 'bv,ba' -o '%(title)s.f%(format_id)s.%(ext)s'

# Download and merge the best format that has a video stream,
# and all audio-only formats into one file
$ yt-dlp -f 'bv*+mergeall[vcodec=none]' --audio-multistreams

# Download and merge the best format that has a video stream,
# and the best 2 audio-only formats into one file
$ yt-dlp -f 'bv*+ba+ba.2' --audio-multistreams


# The following examples show the old method (without -S) of format selection
# and how to use -S to achieve a similar but (generally) better result

# Download the worst video available (old method)
$ yt-dlp -f 'wv*+wa/w'

# Download the best video available but with the smallest resolution
$ yt-dlp -S '+res'

# Download the smallest video available
$ yt-dlp -S '+size,+br'



# Download the best mp4 video available, or the best video if no mp4 available
$ yt-dlp -f 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b'

# Download the best video with the best extension
# (For video, mp4 > webm > flv. For audio, m4a > aac > mp3 ...)
$ yt-dlp -S 'ext'



# Download the best video available but no better than 480p,
# or the worst video if there is no video under 480p
$ yt-dlp -f 'bv*[height<=480]+ba/b[height<=480] / wv*+ba/w'

# Download the best video available with the largest height but no better than 480p,
# or the best video with the smallest resolution if there is no video under 480p
$ yt-dlp -S 'height:480'

# Download the best video available with the largest resolution but no better than 480p,
# or the best video with the smallest resolution if there is no video under 480p
# Resolution is determined by using the smallest dimension.
# So this works correctly for vertical videos as well
$ yt-dlp -S 'res:480'



# Download the best video (that also has audio) but no bigger than 50 MB,
# or the worst video (that also has audio) if there is no video under 50 MB
$ yt-dlp -f 'b[filesize<50M] / w'

# Download largest video (that also has audio) but no bigger than 50 MB,
# or the smallest video (that also has audio) if there is no video under 50 MB
$ yt-dlp -f 'b' -S 'filesize:50M'

# Download best video (that also has audio) that is closest in size to 50 MB
$ yt-dlp -f 'b' -S 'filesize~50M'



# Download best video available via direct link over HTTP/HTTPS protocol,
# or the best video available via any protocol if there is no such video
$ yt-dlp -f '(bv*+ba/b)[protocol^=http][protocol!*=dash] / (bv*+ba/b)'

# Download best video available via the best protocol
# (https/ftps > http/ftp > m3u8_native > m3u8 > http_dash_segments ...)
$ yt-dlp -S 'proto'



# Download the best video with h264 codec, or the best video if there is no such video
$ yt-dlp -f '(bv*+ba/b)[vcodec^=avc1] / (bv*+ba/b)'

# Download the best video with best codec no better than h264,
# or the best video with worst codec if there is no such video
$ yt-dlp -S 'codec:h264'

# Download the best video with worst codec no worse than h264,
# or the best video with best codec if there is no such video
$ yt-dlp -S '+codec:h264'



# More complex examples

# Download the best video no better than 720p preferring framerate greater than 30,
# or the worst video (still preferring framerate greater than 30) if there is no such video
$ yt-dlp -f '((bv*[fps>30]/bv*)[height<=720]/(wv*[fps>30]/wv*)) + ba / (b[fps>30]/b)[height<=720]/(w[fps>30]/w)'

# Download the video with the largest resolution no better than 720p,
# or the video with the smallest resolution available if there is no such video,
# preferring larger framerate for formats with the same resolution
$ yt-dlp -S 'res:720,fps'



# Download the video with smallest resolution no worse than 480p,
# or the video with the largest resolution available if there is no such video,
# preferring better codec and then larger total bitrate for the same resolution
$ yt-dlp -S '+res:480,codec,br'
```

# MODIFYING METADATA

The metadata obtained by the extractors can be modified by using `--parse-metadata` and `--replace-in-metadata`

`--replace-in-metadata FIELDS REGEX REPLACE` is used to replace text in any metadata field using [python regular expression](https://docs.python.org/3/library/re.html#regular-expression-syntax). [Backreferences](https://docs.python.org/3/library/re.html?highlight=backreferences#re.sub) can be used in the replace string for advanced use.

The general syntax of `--parse-metadata FROM:TO` is to give the name of a field or an [output template](#output-template) to extract data from, and the format to interpret it as, separated by a colon `:`. Either a [python regular expression](https://docs.python.org/3/library/re.html#regular-expression-syntax) with named capture groups or a similar syntax to the [output template](#output-template) (only `%(field)s` formatting is supported) can be used for `TO`. The option can be used multiple times to parse and modify various fields.

Note that any field created by this can be used in the [output template](#output-template) and will also affect the media file's metadata added when using `--add-metadata`.

This option also has a few special uses:
* You can download an additional URL based on the metadata of the currently downloaded video. To do this, set the field `additional_urls` to the URL that you want to download. Eg: `--parse-metadata "description:(?P<additional_urls>https?://www\.vimeo\.com/\d+)` will download the first vimeo video found in the description
* You can use this to change the metadata that is embedded in the media file. To do this, set the value of the corresponding field with a `meta_` prefix. For example, any value you set to `meta_description` field will be added to the `description` field in the file. For example, you can use this to set a different "description" and "synopsis". Any value set to the `meta_` field will overwrite all default values.

For reference, these are the fields yt-dlp adds by default to the file metadata:

Metadata fields|From
:---|:---
`title`|`track` or `title`
`date`|`upload_date`
`description`,  `synopsis`|`description`
`purl`, `comment`|`webpage_url`
`track`|`track_number`
`artist`|`artist`, `creator`, `uploader` or `uploader_id`
`genre`|`genre`
`album`|`album`
`album_artist`|`album_artist`
`disc`|`disc_number`
`show`|`series`
`season_number`|`season_number`
`episode_id`|`episode` or `episode_id`
`episode_sort`|`episode_number`
`language` of each stream|From the format's `language`
**Note**: The file format may not support some of these fields


## Modifying metadata examples

Note that on Windows you may need to use double quotes instead of single.

```bash
# Interpret the title as "Artist - Title"
$ yt-dlp --parse-metadata 'title:%(artist)s - %(title)s'

# Regex example
$ yt-dlp --parse-metadata 'description:Artist - (?P<artist>.+)'

# Set title as "Series name S01E05"
$ yt-dlp --parse-metadata '%(series)s S%(season_number)02dE%(episode_number)02d:%(title)s'

# Set "comment" field in video metadata using description instead of webpage_url
$ yt-dlp --parse-metadata 'description:(?s)(?P<meta_comment>.+)' --add-metadata

# Remove "formats" field from the infojson by setting it to an empty string
$ yt-dlp --parse-metadata ':(?P<formats>)' -j

# Replace all spaces and "_" in title and uploader with a `-`
$ yt-dlp --replace-in-metadata 'title,uploader' '[ _]' '-'

```

# EXTRACTOR ARGUMENTS

Some extractors accept additional arguments which can be passed using `--extractor-args KEY:ARGS`. `ARGS` is a `;` (semicolon) separated string of `ARG=VAL1,VAL2`. Eg: `--extractor-args "youtube:player-client=android_agegate,web;include_live_dash" --extractor-args "funimation:version=uncut"`

The following extractors use this feature:

#### youtube
* `skip`: `hls` or `dash` (or both) to skip download of the respective manifests
* `player_client`: Clients to extract video data from. The main clients are `web`, `android`, `ios`, `mweb`. These also have `_music`, `_embedded`, `_agegate`, and `_creator` variants (Eg: `web_embedded`) (`mweb` has only `_agegate`). By default, `android,web` is used, but the agegate and creator variants are added as required for age-gated videos. Similarly the music variants are added for `music.youtube.com` urls. You can also use `all` to use all the clients, and `default` for the default clients.
* `player_skip`: Skip some network requests that are generally needed for robust extraction. One or more of `configs` (skip client configs), `webpage` (skip initial webpage), `js` (skip js player). While these options can help reduce the number of requests needed or avoid some rate-limiting, they could cause some issues. See [#860](https://github.com/yt-dlp/yt-dlp/pull/860) for more details
* `include_live_dash`: Include live dash formats (These formats don't download properly)
* `comment_sort`: `top` or `new` (default) - choose comment sorting mode (on YouTube's side)
* `max_comments`: Maximum amount of comments to download (default all)
* `max_comment_depth`: Maximum depth for nested comments. YouTube supports depths 1 or 2 (default)
* `preferred_langs`: List of languages (in 2-charactor code) to prefer for title and description, separated by comma. Original title and description based on your region or settings are still available at `orig_*` key. (See [output template](#output-template) section for these keys)

#### youtubetab (YouTube playlists, channels, feeds, etc.)
* `skip`: One or more of `webpage` (skip initial webpage download), `authcheck` (allow the download of playlists requiring authentication when no initial webpage is downloaded. This may cause unwanted behavior, see [#1122](https://github.com/yt-dlp/yt-dlp/pull/1122) for more details)

#### funimation
* `language`: Languages to extract. Eg: `funimation:language=english,japanese`
* `version`: The video version to extract - `uncut` or `simulcast`

#### crunchyroll
* `language`: Languages to extract. Eg: `crunchyroll:language=jaJp`
* `hardsub`: Which hard-sub versions to extract. Eg: `crunchyroll:hardsub=None,enUS`

#### vikichannel
* `video_types`: Types of videos to download - one or more of `episodes`, `movies`, `clips`, `trailers`

#### niconico
* `segment_duration` *1: Changes segment duration (in **milliseconds**) for DMC formats. Only have effects for HLS formats.
* `player_size`: Modifies the simulated size of player, needed to convert comments to subtitles. `16:9`, `4:3` and size specification (`WIDTHxHEIGHT`) are accepted.

#### niconicolive (niconico:live)
* `latency`: Latency option either `high` or `low`. Default is `low`.
* `format_set`: Reserved.

#### y2mate
* `mode`: Changes mode for extraction. One of `normal` and `rush`. Defaults to `normal`.

#### youtubewebarchive
* `check_all`: Try to check more at the cost of more requests. One or more of `thumbnails`, `captures`


NOTE: These options may be changed/removed in the future without concern for backward compatibility

*1: **READ CAREFULLY**: Using it will make non-standard DMC request(s). You may be being banned of your account or IP address by using it. Use it at your own risk. <!-- It's better to use this option with `-N` if you really don't mind. -->


# PLUGINS

Plugins are loaded from `<root-dir>/ytdlp_plugins/<type>/__init__.py`; where `<root-dir>` is the directory of the binary (`<root-dir>/yt-dlp`), or the root directory of the module if you are running directly from source-code (`<root dir>/yt_dlp/__main__.py`). Plugins are currently not supported for the `pip` version

Plugins can be of `<type>`s `extractor` or `postprocessor`. Extractor plugins do not need to be enabled from the CLI and are automatically invoked when the input URL is suitable for it. Postprocessor plugins can be invoked using `--use-postprocessor NAME`.

See [ytdlp_plugins](ytdlp_plugins) for example plugins.

Note that **all** plugins are imported even if not invoked, and that **there are no checks** performed on plugin code. Use plugins at your own risk and only if you trust the code

If you are a plugin author, add [ytdlp-plugins](https://github.com/topics/ytdlp-plugins) as a topic to your repository for discoverability



# EMBEDDING YT-DLP

yt-dlp makes the best effort to be a good command-line program, and thus should be callable from any programming language.

Your program should avoid parsing the normal stdout since they may change in future versions. Instead they should use options such as `-J`, `--print`, `--progress-template`, `--exec` etc to create console output that you can reliably reproduce and parse.

From a Python program, you can embed yt-dlp in a more powerful fashion, like this:

```python
from yt_dlp import YoutubeDL

ydl_opts = {'format': 'bestaudio'}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
```

Most likely, you'll want to use various options. For a list of options available, have a look at [`yt_dlp/YoutubeDL.py`](yt_dlp/YoutubeDL.py#L162).

Here's a more complete example demonstrating various functionality:

```python
import json
import yt_dlp


class MyLogger:
    def debug(self, msg):
        # For compatability with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


# ℹ️ See the docstring of yt_dlp.postprocessor.common.PostProcessor
class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    # ℹ️ See docstring of yt_dlp.postprocessor.common.PostProcessor.run
    def run(self, info):
        self.to_screen('Doing stuff')
        return [], info


# ℹ️ See "progress_hooks" in the docstring of yt_dlp.YoutubeDL
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def format_selector(ctx):
    """ Select the best video and the best audio that won't result in an mkv.
    This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    yield {
        # These are the minimum required fields for a merged format
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        # Must be + seperated list of protocols
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }


# ℹ️ See docstring of yt_dlp.YoutubeDL for a description of the options
ydl_opts = {
    'format': format_selector,
    'postprocessors': [{
        # Embed metadata in video using ffmpeg.
        # ℹ️ See yt_dlp.postprocessor.FFmpegMetadataPP for the arguments it accepts
        'key': 'FFmpegMetadata',
        'add_chapters': True,
        'add_metadata': True,
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


# Add custom headers
yt_dlp.utils.std_headers.update({'Referer': 'https://www.google.com'})

# ℹ️ See the public functions in yt_dlp.YoutubeDL for for other available functions.
# Eg: "ydl.download", "ydl.download_with_info_file"
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.add_post_processor(MyCustomPP())
    info = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc')

    # ℹ️ ydl.sanitize_info makes the info json-serializable
    print(json.dumps(ydl.sanitize_info(info)))
```

**Tip**: If you are porting your code from youtube-dl to yt-dlp, one important point to look out for is that we do not guarantee the return value of `YoutubeDL.extract_info` to be json serializable, or even be a dictionary. It will be dictionary-like, but if you want to ensure it is a serializable dictionary, pass it through `YoutubeDL.sanitize_info` as shown in the example above


# DEPRECATED OPTIONS

These are all the deprecated options and the current alternative to achieve the same effect

#### Redundant options
While these options are redundant, they are still expected to be used due to their ease of use

    --get-description                --print description
    --get-duration                   --print duration_string
    --get-filename                   --print filename
    --get-format                     --print format
    --get-id                         --print id
    --get-thumbnail                  --print thumbnail
    -e, --get-title                  --print title
    -g, --get-url                    --print urls
    -j, --dump-json                  --print "%()j"
    --match-title REGEX              --match-filter "title ~= (?i)REGEX"
    --reject-title REGEX             --match-filter "title !~= (?i)REGEX"
    --min-views COUNT                --match-filter "view_count >=? COUNT"
    --max-views COUNT                --match-filter "view_count <=? COUNT"


#### Not recommended
While these options still work, their use is not recommended since there are other alternatives to achieve the same

    --all-formats                    -f all
    --all-subs                       --sub-langs all --write-subs
    --print-json                     -j --no-simulate
    --autonumber-size NUMBER         Use string formatting. Eg: %(autonumber)03d
    --autonumber-start NUMBER        Use internal field formatting like %(autonumber+NUMBER)s
    --id                             -o "%(id)s.%(ext)s"
    --metadata-from-title FORMAT     --parse-metadata "%(title)s:FORMAT"
    --hls-prefer-native              --downloader "m3u8:native"
    --hls-prefer-ffmpeg              --downloader "m3u8:ffmpeg"
    --list-formats-old               --compat-options list-formats (Alias: --no-list-formats-as-table)
    --list-formats-as-table          --compat-options -list-formats [Default] (Alias: --no-list-formats-old)
    --youtube-skip-dash-manifest     --extractor-args "youtube:skip=dash" (Alias: --no-youtube-include-dash-manifest)
    --youtube-skip-hls-manifest      --extractor-args "youtube:skip=hls" (Alias: --no-youtube-include-hls-manifest)
    --youtube-include-dash-manifest  Default (Alias: --no-youtube-skip-dash-manifest)
    --youtube-include-hls-manifest   Default (Alias: --no-youtube-skip-hls-manifest)


#### Developer options
These options are not intended to be used by the end-user

    --test                           Download only part of video for testing extractors
    --youtube-print-sig-code         For testing youtube signatures
    --allow-unplayable-formats       List unplayable formats also
    --no-allow-unplayable-formats    Default


#### Old aliases
These are aliases that are no longer documented for various reasons

    --avconv-location                --ffmpeg-location
    --cn-verification-proxy URL      --geo-verification-proxy URL
    --dump-headers                   --print-traffic
    --dump-intermediate-pages        --dump-pages
    --force-write-download-archive   --force-write-archive
    --load-info                      --load-info-json
    --no-split-tracks                --no-split-chapters
    --no-write-srt                   --no-write-subs
    --prefer-unsecure                --prefer-insecure
    --rate-limit RATE                --limit-rate RATE
    --split-tracks                   --split-chapters
    --srt-lang LANGS                 --sub-langs LANGS
    --trim-file-names LENGTH         --trim-filenames LENGTH
    --write-srt                      --write-subs
    --yes-overwrites                 --force-overwrites

#### Sponskrub Options
Support for [SponSkrub](https://github.com/faissaloo/SponSkrub) has been deprecated in favor of the `--sponsorblock` options

    --sponskrub                      --sponsorblock-mark all
    --no-sponskrub                   --no-sponsorblock
    --sponskrub-cut                  --sponsorblock-remove all
    --no-sponskrub-cut               --sponsorblock-remove -all
    --sponskrub-force                Not applicable
    --no-sponskrub-force             Not applicable
    --sponskrub-location             Not applicable
    --sponskrub-args                 Not applicable

#### No longer supported
These options may no longer work as intended

    --prefer-avconv                  avconv is not officially supported by yt-dlp (Alias: --no-prefer-ffmpeg)
    --prefer-ffmpeg                  Default (Alias: --no-prefer-avconv)
    -C, --call-home                  Not implemented
    --no-call-home                   Default
    --include-ads                    No longer supported
    --no-include-ads                 Default
    --write-annotations              No supported site has annotations now
    --no-write-annotations           Default

#### Removed
These options were deprecated since 2014 and have now been entirely removed

    -A, --auto-number                -o "%(autonumber)s-%(id)s.%(ext)s"
    -t, --title                      -o "%(title)s-%(id)s.%(ext)s"
    -l, --literal                    -o accepts literal names

# CONTRIBUTING
See [CONTRIBUTING.md](CONTRIBUTING.md#contributing-to-yt-dlp) for instructions on [Opening an Issue](CONTRIBUTING.md#opening-an-issue) and [Contributing code to the project](CONTRIBUTING.md#developer-instructions)

# MORE
For FAQ see the [youtube-dl README](https://github.com/ytdl-org/youtube-dl#faq)
