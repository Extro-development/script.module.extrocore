################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2013 Stephan Raue (stephan@openelec.tv)
#      Copyright (C) 2013 Lutz Fiebach (lufie@openelec.tv)
#
#  This program is dual-licensed; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC; see the file COPYING.  If not, see
#  <http://www.gnu.org/licenses/>.
#
#  Alternatively, you can license this library under a commercial license,
#  please contact OpenELEC Licensing for more information.
#
#  For more information contact:
#  OpenELEC Licensing  <license@openelec.tv>  http://www.openelec.tv
################################################################################

ADDON_NAME=script.module.extrocore

BUILDDIR=build
DATADIR=/usr/share/kodi
ADDONDIR=$(DATADIR)/addons

################################################################################

all: $(BUILDDIR)/$(ADDON_NAME)

addon: $(BUILDDIR)/$(ADDON_NAME)-$(ADDON_VERSION).zip

install: $(BUILDDIR)/$(ADDON_NAME)
	mkdir -p $(DESTDIR)$(ADDONDIR)
	cp -R $(BUILDDIR)/$(ADDON_NAME) $(DESTDIR)$(ADDONDIR)

clean:
	rm -rf $(BUILDDIR)

uninstall:
	rm -rf $(DESTDIR)$(ADDONDIR)/$(ADDON_NAME)

$(BUILDDIR)/$(ADDON_NAME): $(BUILDDIR)/$(ADDON_NAME)/lib
	mkdir -p $(BUILDDIR)/$(ADDON_NAME)
	cp -R *.py $(BUILDDIR)/$(ADDON_NAME)
	cp LICENSE.txt $(BUILDDIR)/$(ADDON_NAME)
	cp addon.xml $(BUILDDIR)/$(ADDON_NAME)

$(BUILDDIR)/$(ADDON_NAME)/lib:
	mkdir -p $(BUILDDIR)/$(ADDON_NAME)/lib
	cp -R lib/* $(BUILDDIR)/$(ADDON_NAME)/lib

$(BUILDDIR)/$(ADDON_NAME)-$(ADDON_VERSION).zip: $(BUILDDIR)/$(ADDON_NAME)
	cd $(BUILDDIR); zip -r $(ADDON_NAME)-$(ADDON_VERSION).zip $(ADDON_NAME)
