/*Copyright (c) 2013 Jacques Menuet

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

#pragma once

#include "PolstroSerialInterface.h"

#include <windows.h>

namespace Polstro
{

class SerialInterfaceWindows : public SerialInterface
{
public:
	SerialInterfaceWindows( const std::string& portName, unsigned int baudRate );
	virtual ~SerialInterfaceWindows();

	virtual bool isOpen() const;

private:
	static HANDLE openPort( const std::string& portName, unsigned int baudRate );
	
	virtual bool writeBytes( const unsigned char* data, unsigned int dataSizeInBytes );
	virtual bool readBytes( unsigned char* data, unsigned int dataSizeInBytes );

	HANDLE	mPortHandle;
};

}
