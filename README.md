<p align="center">
  <img width="100%" src="https://github.com/robolab-io/iohook/assets/52982404/edec7f92-70bc-43bf-9ec8-19a0a1be7921"/>
</p>

iohook is a global native keyboard and mouse listener for Node.js. This is a fork of https://github.com/wilix-team/iohook, which is abandoned and unmainntained.

We provide a modern CI pipeline for easy, fast, reliable, builds of iohook for modern versions of Node and Electron. At Robolab, we use this library in [MechaKeys](https://v2.robolab.io), the integrated typing environment.

## Supported Versions
- Versions >= 0.9.4 support Electron 25 and Node 18
- For older version support, use the wilix-team library

## Installation
```sh
# Install MechaKeys iohook
npm install --save @mechakeys/iohook
```

```sh
# Install prebuilt binaries for your platform, architecture, and ABIs.
cd ./node_modules/@mechakeys/iohook
npm i
node install.js
```

By default, prebuilds will be downloaded for your own platform and architecture, but you can download specific ones through your package.json:
```json
"iohook": {
    "targets": [
        "node-108",
        "electron-116"
    ],
    "platforms": [
        "win32",
        "darwin",
        "linux"
    ],
    "arches": [
        "x64",
    ]
}
```

As of right now, we do not build 32-bit versions.
