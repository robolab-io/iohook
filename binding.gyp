{
	"targets": [{
		"target_name": "iohook",
		"win_delay_load_hook": "true",
		"type": "loadable_module",
		"sources": [
			"src/iohook.cc",
			"src/iohook.h"
		],
		"dependencies": [
			"./uiohook.gyp:uiohook"
		],
		"include_dirs": [
			"<!(node -e \"require('nan')\")",
			"libuiohook/include"
		],
        'xcode_settings': {
			'CLANG_CXX_LANGUAGE_STANDARD': 'c++17'
		}
		"configurations": {
			"Release": {
				"msvs_settings": {
					"VCCLCompilerTool": {
						'ExceptionHandling': 1
					}
				}
			}
		}
	}]
}
