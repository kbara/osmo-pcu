#!/usr/bin/env python

# (C) 2013 by Katerina Barone-Adesi <kat.obsc@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

app_configs = {
    "osmo-pcu": ["examples/osmo-pcu.cfg"]
}

apps = [(4240, "src/osmo-pcu", "Osmo-PCU", "osmo-pcu"),
        ]

vty_command = ["src/osmo-pcu", "-c", "examples/osmo-pcu.cfg"]

vty_app = apps[0]
