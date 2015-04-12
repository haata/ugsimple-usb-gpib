#!/usr/bin/env python3

# Copyright (C) 2015 by Jacob Alexander
#
# This file is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.

### Imports ###

from ugsimple.GPIB import UGSimpleGPIB



### Program Entry Point ###

if __name__ == '__main__':
	mygpib = UGSimpleGPIB()
	#mygpib = UGSimpleGPIB(debug_mode=True)

	print ( mygpib.firmware_version() )
	print ( mygpib.manufacturer_id() )
	print ( mygpib.series_number() )

	#print ( mygpib.write( 0x02, "*CLS" ) )
	#print ( mygpib.write( 0x03, ":data:fresh?" ) )
	#mygpib.write( 0x02, "*ESE?" )
	#mygpib.write( 0x02, "*ESE" )
	#mygpib.write( 0x03, "*IDN?" )
	#print ( mygpib.read( 0x03 ) )
	#print ( mygpib.read( 0x02 ) )
	#print ( mygpib.read( 0x02 ) )
	#print ( mygpib.read( 0x03 ) )


