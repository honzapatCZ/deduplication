{
  "targets": [
    {
      "target_name": "binding",
      "sources": [ "binding.cc" ],
      "include_dirs": [ "<!(node -e \"require('nan')\")" ],
			"defines": [
        "OPENSSL_API_COMPAT=0x10100001L",
        "OPENSSL_CONFIGURED_API=0x30000000L"
			],
    },
    {
      "target_name": "copy",
      "type": "none",
      "dependencies": [ "binding" ],
      "copies": [
        {
          'destination': '<(module_root_dir)',
          'files': ['<(module_root_dir)/build/Release/binding.node']
        }
      ]
    }
  ]
}
