# REVISION : can be obtained from http://omahaproxy.appspot.com/ (branch_base_position)
# http://commondatastorage.googleapis.com/chromium-browser-continuous/index.html?prefix=Linux_x64/
# or http://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Linux_x64/
REVISION = 394941
CHROMIUM_URL = https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F$(REVISION)%2Fchrome-linux.zip?alt=media

all: tarball

tarball:
	wget $(CHROMIUM_URL) -O Linux_x64-$(REVISION)-chrome-linux.zip

clean:
	git clean -ffd

.PHONY: all tarball clean
