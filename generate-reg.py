import os
import codecs

path=rf'''Users\\{os.environ['USERNAME']}\\AppData\\Local\\pyBrowserSelection\\bin'''

outbuff = rf'''Windows Registry Editor Version 5.00
;this follows the steps described in 
;https://kolbi.cz/blog/2019/01/27/register-a-portable-browser-and-make-it-the-default/
;this is a sample file
;make sure you edit the content to match your system configuratiot
;usually replacing PATH_TO_YOUR_INSTALLATION_OF to your actual installation path should be enough

[HKEY_CURRENT_USER\SOFTWARE\RegisteredApplications]
"pyBrowserSelection"="Software\\Clients\\StartMenuInternet\\pyBrowserSelection\\Capabilities"




[HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection]

 [HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection\Capabilities]
"ApplicationDescription"="pyBrowserSelection"
"ApplicationIcon"="C:\\{path}\\pyBrowserSelection.exe,0"
"ApplicationName"="pyBrowserSelection"

 [HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection\Capabilities\FileAssociations]
; you can add additional filetypes like .pdf if your browser supports it
".htm"="pyBrowserSelectionHTM"
".html"="pyBrowserSelectionHTM"

 [HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection\Capabilities\Startmenu]
"StartMenuInternet"="pyBrowserSelection"

 [HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection\Capabilities\URLAssociations]
; you can add additional protocols like mailto for example
"http"="pyBrowserSelectionHTM"
"https"="pyBrowserSelectionHTM"

 [HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection\DefaultIcon]
@="C:\\{path}\\pyBrowserSelection.exe,0"

[HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection\shell]

[HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection\shell\open]

[HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\pyBrowserSelection\shell\open\command]
@="\"C:\\{path}\\pyBrowserSelection.exe\""




[HKEY_CURRENT_USER\SOFTWARE\Classes\pyBrowserSelectionHTM]
@="pyBrowserSelection Handler"
"AppUserModelId"="pyBrowserSelection"

[HKEY_CURRENT_USER\SOFTWARE\Classes\pyBrowserSelectionHTM\Application]
"AppUserModelId"="pyBrowserSelection"
"ApplicationIcon"="C:\\{path}\\pyBrowserSelection.exe,0"
"ApplicationName"="pyBrowserSelection"
"ApplicationDescription"="Select Browser on-the-fly"
"ApplicationCompany"="pyBrowserSelection Portable"

[HKEY_CURRENT_USER\SOFTWARE\Classes\pyBrowserSelectionHTM\DefaultIcon]
@="ApplicationIcon"="C:\\{path}\\pyBrowserSelection.exe,0"

[HKEY_CURRENT_USER\SOFTWARE\Classes\pyBrowserSelectionHTM\shell]
[HKEY_CURRENT_USER\SOFTWARE\Classes\pyBrowserSelectionHTM\shell\open]
[HKEY_CURRENT_USER\SOFTWARE\Classes\pyBrowserSelectionHTM\shell\open\command]
; your browser might offer different arguments here - %1 opens just the argument given
@="\"C:\\{path}\\pyBrowserSelection.exe\" \"%1\""
'''

# with open('myfile.reg', 'x', encoding='UTF-16le') as regfile:
with open('myfile.reg', 'x+b') as regfile:
    regfile.write(codecs.BOM_UTF16_LE)
with open('myfile.reg', 'a', encoding='UTF-16le') as regfile:
    regfile.write(outbuff)

