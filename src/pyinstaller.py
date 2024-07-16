import PyInstaller.__main__

PyInstaller.__main__.run([
    'sockettesting.py',
    '--onefile',
    '--windowed',
    '--hidden-import=eventlet.hubs.epolls',
    '--hidden-import=eventlet.hubs.kqueue',
    '--hidden-import=eventlet.hubs.selects',
    '--hidden-import=gevent',
    '--hidden-import=engineio.async_drivers.gevent',
    '--hidden-import=engineio.async_drivers.eventlet',
    '--hidden-import=engineio.async_drivers.threading',
    '--hidden-import=dns.dns',
    '--hidden-import=dns.dnssec',
    '--hidden-import=dns.e164',
    '--hidden-import=dns.hash',
    '--hidden-import=dns.namedict',
    '--hidden-import=dns.tsigkeyring',
    '--hidden-import=dns.tsigkeyring',
    '--hidden-import=dns.update',
    '--hidden-import=dns.version',
    '--hidden-import=dns.zone',
    '--hidden-import=dns.dnssec',
    '--hidden-import=dns.asyncquery',
    '--hidden-import=dns.asyncresolver',
    '--hidden-import=dns.versioned'
])