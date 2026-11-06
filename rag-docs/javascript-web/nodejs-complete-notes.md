---
title: NODEJS-COMPLETE-NOTES
topic: javascript-web
source_type: my-notes
source_file: STUDYNOTEs/NODEJS-COMPLETE-NOTES.md
---

# Node.js + Express.js — Complete Beginner Notes

**Compiled from every PDF in `nodejsnotesfolder/` (read-only; no source file was modified).**

## About the sources

| File | Pages | Content |
|---|---|---|
| `1688581742241.pdf` and `1688581742241 (1).pdf` | 45 | Identical copies. Handwritten "Complete Notes on Node.js" — cover, index, notebook pages 1–42 |
| `1752211828477.pdf` | 86 | Same handwritten notebook, **complete**: cover, index, notebook pages 1–83 |
| `1755022766998.pdf` and `nodejsnotes.pdf` | 86 | Identical copies of the same complete Node.js notebook |
| `1770624422879.pdf` | 51 | Handwritten **Express.js** notebook — cover, index, pages 1–50 |

So there are only **two distinct notebooks**: one on Node.js (83 pages) and one on Express.js (50 pages). Everything else is a duplicate.

Both notebooks are credited to: *Mayuri Kishor Khavche (Software Engineer)* — Instagram @codes.learning, YouTube "Point of Programming", Telegram Codeslearning. The material follows the JavaTpoint Node.js/Express.js tutorial, so all examples use "JavaTpoint" strings and `javatpoint` sample data.

**Note on interview questions:** you asked me to separate the notes from the interview questions. **None of the PDFs contain interview questions** — all six files are tutorial notes. To still give you that section, Part C below is an interview Q&A built *only* from the facts written in these two notebooks; it is clearly marked as derived, not transcribed.

**One gap in the source:** the Express notebook jumps from handwritten page 45 to page 47 (page 46 is not in the scan). Nothing else is missing.

---

# How to read this document

- **Part A — Node.js** (notebook 1, pages 1–83): what Node is, core modules, files, streams, buffers, events, databases.
- **Part B — Express.js** (notebook 2, pages 1–50): the web framework built on top of Node.
- **Part C — Interview questions** derived from Parts A and B.

Each part goes in the same order as the notebooks, so you can learn step by step. Code is shown exactly as written in the notes (they use the older `var` / `new Buffer` style; modern equivalents are pointed out in the *Modern note* boxes so you are not confused when you read today's documentation).

---

# PART A — NODE.JS

## A1. What is Node.js

Node.js is an **open-source, cross-platform runtime environment** for developing server-side and networking applications. Node.js applications are written in JavaScript and run inside the Node.js runtime on OS X, Microsoft Windows and Linux.

The key idea:

```
Node.js = JavaScript Runtime Environment + JavaScript Library
```

A browser runs JavaScript to make web pages interactive. Node takes the same JavaScript language and lets it run **outside the browser**, on a server, where it can read files, talk to databases and answer HTTP requests.

### The 7 features of Node.js (from page 1–2)

1. **Extremely fast** — built on Google Chrome's **V8** JavaScript engine, so code execution is very fast.
2. **I/O is asynchronous and event driven** — all APIs of the Node.js library are asynchronous (non-blocking). A Node.js based server never waits for an API to return data: it moves to the next API after calling it, and a **notification mechanism of events** helps it get the response from the previous API call.
3. **Single threaded** — Node.js follows a single threaded model with **event looping**.
4. **Highly scalable** — because events help the server respond in a non-blocking way, it is highly scalable. Node uses a single threaded program that can serve a much larger number of requests than a traditional server like Apache HTTP Server.
5. **No buffering** — Node.js applications never buffer any data; they simply **output the data in chunks**.
6. **Open source** — Node.js has a big open source community which has produced many excellent modules to add extra capabilities to Node.js applications.
7. **License** — Node.js is released under the **MIT license**.

### Parts of Node.js (page 3)

The notebook lists the pieces you will meet as you learn:

Buffer · Streaming · DNS · Domain · Global · Net · Modules · Error Handling · Debugger · Console · Cluster · Add-ons · Callback · Crypto

---

## A2. Installing Node.js and your first programs

### What you need (page 3–4)

To develop Node.js applications on Windows you need only two things:

1. **A text editor** — e.g. Notepad, Notepad++, VIM, Sublime Text.
2. **The Node.js binary installer** — download from `https://nodejs.org/en/download/`.

Source files are written in JavaScript and saved with the **`.js`** extension. The Node.js runtime interprets and executes them.

### First example — console based (page 4)

File: `console_example1.js`

```js
console.log("Hello JavaTpoint");
```

Run it from the Node.js command prompt:

```bash
node console_example1.js
```

Output:

```
Hello JavaTpoint
```

### Second example — web based (page 5–6)

A Node.js web application has **three parts**:

1. **Import required modules** — use the `require` directive to load Node.js modules.
2. **Create server** — a server which will listen to the client's requests, similar to Apache HTTP Server.
3. **Read request and return response** — the server created in the earlier step reads the HTTP request made by the client (which can be a browser or a console) and returns the response.

File: `main.js`

```js
var http = require("http");

http.createServer(function (request, response) {
   // Send the HTTP header
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});

   // Send the response body as "Hello World"
   response.end('Hello World\n');
}).listen(8081);

// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');
```

Run `node main.js`, then open `http://127.0.0.1:8081/` in a browser — you will see **Hello World**.

**Reading the code:**
- `require("http")` loads Node's built-in HTTP module.
- `createServer(callback)` registers a function that runs on *every* incoming request.
- `writeHead(200, {...})` sends the status code and headers.
- `response.end(...)` sends the body and finishes the response.
- `listen(8081)` starts listening on port 8081.

---

## A3. The Console module (page 6–8)

The console module provides a simple debugging console, like the JavaScript console of a web browser. Three methods are used most:

| Method | Purpose |
|---|---|
| `console.log()` | Prints to stdout with a newline. Supports `printf`-style format specifiers. |
| `console.error()` | Prints to stderr with a newline. |
| `console.warn()` | Prints a warning to stderr. |

**`console.log()` with a format specifier:**

```js
console.log('Hello %s', 'JavaTpoint');   // Hello JavaTpoint
```

**`console.error()`:**

```js
console.error(new Error('Hell! This is a wrong method.'));
```

**`console.warn()` with a template literal:**

```js
const name = 'JavaTpoint';
console.warn(`Warning: ${name} is deprecated`);
```

---

## A4. REPL — the interactive shell (page 8–11)

**REPL stands for Read Eval Print Loop.** It is the console/shell where you can type JavaScript and see the result immediately. Node ships with a REPL: just type `node` with no filename.

The four steps in the name:

| Step | Meaning |
|---|---|
| **Read** | Reads the user's input, parses it into a JavaScript data structure, and stores it in memory. |
| **Eval** | Takes the data structure and evaluates it. |
| **Print** | Prints the result produced by evaluating the command. |
| **Loop** | Loops the above command until the user presses `Ctrl+C` twice. |

### Simple expressions

```
> 10 + 20 - 5
25
```

### Using variables

```
> x = 10          // prints 10 (assignment without var echoes the value)
10
> var x = 10      // prints undefined (a var declaration evaluates to undefined)
undefined
> var a = 40, b = 60
undefined
> a + b
100
```

This is a classic beginner trap: `var x = 10` prints `undefined` because a *declaration* has no value; `x = 10` prints `10` because an *assignment expression* evaluates to the assigned value.

### Multiline expressions

The REPL detects an incomplete block and continues on the next line with `...`:

```
> var x = 0
> do {
...   x++;
...   console.log("x: " + x);
... } while (x < 10);
```

### The underscore variable

`_` holds the result of the **last** expression:

```
> var x = 10
> var y = 20
> x + y
30
> var sum = _
> console.log(sum)
30
```

### REPL commands (page 10–11)

| Command | What it does |
|---|---|
| `Ctrl + C` | Terminate the current command |
| `Ctrl + C` (twice) | Terminate the REPL |
| `Ctrl + D` | Terminate the REPL |
| Up / Down arrows | Browse command history and modify previous commands |
| `Tab` | List the current commands / autocomplete |
| `.help` | List all the commands |
| `.break` | Exit from a multi-line expression |
| `.clear` | Exit from a multi-line expression |
| `.save filename` | Save the current REPL session to a file |
| `.load filename` | Load the given file into the current REPL session |

**To exit the REPL: press `Ctrl + C` twice.**

---

## A5. NPM — Node Package Manager (page 11–12)

NPM (Node Package Manager) provides **two main functionalities**:

1. **Online repositories** for Node.js packages/modules, which are searchable on `search.nodejs.org`.
2. A **command line utility** to install Node.js packages, and to do version management and dependency management of Node.js packages.

NPM comes **bundled with Node.js installables** after version **v0.6.3**. To verify:

```bash
npm version
```

### Installing, uninstalling and searching modules

```bash
npm install <ModuleName>        # install a module
npm install express             # e.g. install express
npm uninstall express           # uninstall a module
npm search express              # search for a module
```

---

## A6. Node.js command line options (page 12–15)

| # | Option | Description |
|---|---|---|
| 1 | `-v`, `--version` | Print node's version |
| 2 | `-h`, `--help` | Print node command line options |
| 3 | `-e`, `--eval "script"` | Evaluate the following argument as JavaScript |
| 4 | `-p`, `--print "script"` | Identical to `-e` but also prints the result |
| 5 | `-c`, `--check` | Syntax check the script without executing |
| 6 | `-i`, `--interactive` | Open the REPL even if stdin does not appear to be a terminal |
| 7 | `-r`, `--require module` | Preload the specified module at startup |
| 8 | `--no-deprecation` | Silence deprecation warnings |
| 9 | `--trace-deprecation` | Print stack traces for deprecations |
| 10 | `--throw-deprecation` | Throw errors for deprecations |
| 11 | `--no-warnings` | Silence all process warnings (including deprecations) |
| 12 | `--trace-warnings` | Print stack traces for process warnings |
| 13 | `--trace-sync-io` | Print a stack trace whenever synchronous I/O is detected after the first turn of the event loop |
| 14 | `--zero-fill-buffers` | Automatically zero-fill all newly allocated Buffer and SlowBuffer instances |
| 15 | `--track-heap-objects` | Track heap object allocations for heap snapshots |
| 16 | `--prof-process` | Process the V8 profiler output generated using the V8 option `--prof` |
| 17 | `--v8-options` | Print V8 command line options |
| 18 | `--tls-cipher-list=list` | Specify an alternative default TLS cipher list |
| 19 | `--enable-fips` | Enable FIPS-compliant crypto at startup |
| 20 | `--force-fips` | Force FIPS-compliant crypto at startup (cannot be disabled from script code) |
| 21 | `--icu-data-dir=file` | Specify the ICU data load path |

---

## A7. Global objects (page 15)

Global objects are available in **all modules** — you do not need to `require()` them. They can be used directly.

| Global | Meaning |
|---|---|
| `__dirname` | The name of the **directory** that the currently executing script lives in |
| `__filename` | The **absolute path** of the file being executed, including the filename |

```js
console.log(__dirname);
console.log(__filename);
```

Other globals covered elsewhere in these notes: `console`, `Buffer`, the timer functions, and `process`.

---

## A8. The OS module (page 16–18)

The OS module provides basic operating-system related utility functions. Load it with `var os = require('os')`.

| # | Method | Returns |
|---|---|---|
| 1 | `os.arch()` | The operating system CPU architecture |
| 2 | `os.cpus()` | An array of objects with information about each CPU/core: model, speed (in MHz), and times (an object with `user`, `nice`, `sys`, `idle`, `irq` in milliseconds) |
| 3 | `os.endianness()` | The endianness of the CPU — `'BE'` for big endian, `'LE'` for little endian |
| 4 | `os.freemem()` | The amount of free system memory in bytes |
| 5 | `os.homedir()` | The home directory of the current user |
| 6 | `os.hostname()` | The hostname of the operating system |
| 7 | `os.loadavg()` | An array containing the 1, 5 and 15 minute load averages |
| 8 | `os.networkInterfaces()` | A list of network interfaces |
| 9 | `os.platform()` | The operating system platform: `'darwin'`, `'win32'`, `'freebsd'`, `'linux'`, `'sunos'` |
| 10 | `os.release()` | The operating system release |
| 11 | `os.tmpdir()` | The operating system's default directory for temporary files |
| 12 | `os.totalmem()` | The total amount of system memory in bytes |
| 13 | `os.type()` | The operating system name: `'Linux'`, `'Darwin'` on OS X, `'Windows_NT'` on Windows |
| 14 | `os.uptime()` | The system uptime in seconds |
| 15 | `os.userInfo([options])` | Information about the currently effective user |

---

## A9. Timers (page 18–20)

Timers are **global** — you do **not** need to `require('timers')`.

### The three timer functions

| Function | Behaviour |
|---|---|
| `setImmediate(callback)` | Runs the callback at the end of the current event loop turn |
| `setInterval(callback, delay)` | Runs the callback **repeatedly**, every `delay` milliseconds |
| `setTimeout(callback, delay)` | Runs the callback **once**, after at least `delay` milliseconds |

### The three cancel functions

| Function | Cancels |
|---|---|
| `clearImmediate(immediateObject)` | A `setImmediate` |
| `clearInterval(intervalObject)` | A `setInterval` |
| `clearTimeout(timeoutObject)` | A `setTimeout` |

### Example — `timer1.js`

```js
setInterval(function () {
    console.log('setInterval: Hey! 1 millisecond completed!.');
}, 1000);
```

This prints the message **every second, forever**, until you stop the program with `Ctrl+C`. (Despite the message text, `1000` means 1000 milliseconds = 1 second.)

---

## A10. Errors and error handling (page 20)

Applications running in Node.js will generally experience **four categories of errors**:

1. **Standard JavaScript errors** —
   - `EvalError` — thrown when a call to `eval()` fails
   - `SyntaxError` — thrown in response to improper JavaScript language syntax
   - `RangeError` — thrown when a value is not within an expected range or set of values
   - `ReferenceError` — thrown when using undefined variables
   - `TypeError` — thrown when passing arguments of the wrong type
   - `URIError` — thrown when a global URI handling function is misused
2. **System errors** — triggered by underlying operating system constraints, such as attempting to open a file that does not exist, or attempting to send data over a closed socket.
3. **User-specified errors** — triggered by application code.
4. **Assertion errors** — a special class of error triggered whenever Node.js detects an exceptional logic violation that should never occur; raised by the `assert` module.

### Example — `error_example1.js`

```js
try {
    const a = 1;
    const c = a + b;      // b is not defined -> ReferenceError
} catch (err) {
    console.log(err);
}
```

The `try ... catch` block prevents the program from crashing and lets you inspect the error object.

---

## A11. The DNS module (page 21–22)

DNS (Domain Name System) resolves hostnames into IP addresses. Load with `const dns = require('dns')`.

| Function | Purpose |
|---|---|
| `dns.getServers()` | Returns an array of IP address strings for the current DNS servers |
| `dns.setServers(servers)` | Sets the IP addresses of the servers to be used when resolving |
| `dns.lookup(hostname[, options], callback)` | Resolves a hostname into the first found A (IPv4) or AAAA (IPv6) record |
| `dns.lookupService(address, port, callback)` | Resolves the given address and port into a hostname and service |
| `dns.resolve(hostname[, rrtype], callback)` | Resolves a hostname into an array of the record types specified by `rrtype` |
| `dns.resolve4(hostname, callback)` | Resolves IPv4 addresses (A records) |
| `dns.resolve6(hostname, callback)` | Resolves IPv6 addresses (AAAA records) |
| `dns.resolveCname(hostname, callback)` | Resolves CNAME records |
| `dns.resolveMx(hostname, callback)` | Resolves mail exchange records |
| `dns.resolveNs(hostname, callback)` | Resolves name server records |
| `dns.resolveSoa(hostname, callback)` | Resolves a start of authority record |
| `dns.resolveSrv(hostname, callback)` | Resolves service records |
| `dns.resolvePtr(hostname, callback)` | Resolves pointer records |
| `dns.resolveTxt(hostname, callback)` | Resolves text queries |
| `dns.reverse(ip, callback)` | Performs a reverse DNS query — resolves an IPv4/IPv6 address to hostnames |

### Example — `dns_example1.js`

```js
const dns = require('dns');

dns.lookup('www.javatpoint.com', (err, addresses, family) => {
    console.log('addresses:', addresses);
    console.log('family:', family);
});
```

Output:

```
addresses: 144.26.11.18
family: 4
```

`family: 4` means the address is IPv4 (`6` would mean IPv6).

---

## A12. The Net module — socket programming (page 22–23)

The Net module is used to create both **servers and clients**. It provides an asynchronous network wrapper and is what you use for socket programming — for example a chat application, where a server and a client talk to each other.

You need **two command prompts** to run this example: one for the server and one for the client.

### Server — `net_server.js`

```js
const net = require('net');

var server = net.createServer((socket) => {
    socket.end('goodbye\n');
}).on('error', (err) => {
    // handle errors here
    throw err;
});

// grab an arbitrary unused port
server.listen(() => {
    address = server.address();
    console.log('opened server on %j', address);
});
```

### Client — `net_client.js`

```js
const net = require('net');

const client = net.connect({port: 50302}, () => {
    // 'connect' listener
    console.log('connected to server!');
    client.write('World!\r\n');
});

client.on('data', (data) => {
    console.log(data.toString());
    client.end();
});

client.on('end', () => {
    console.log('disconnected from server');
});
```

Start the server first, note the port it prints, put that port in the client, then run the client.

---

## A13. The Crypto module (page 24–26)

The crypto module provides **cryptographic functionality**: it is a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign and verify functions.

**Definitions from the notes:**
- **Hash** — a fixed-length string of bits generated from a piece of data. It is **deterministic**: the same input always produces the same hash.
- **HMAC** — Hash-based Message Authentication Code. It is the result of running a hash algorithm over data **plus a secret key**, so only someone with the key can produce or verify it.

### Creating an HMAC — `crypto_example1.js`

```js
const crypto = require('crypto');
const secret = 'abcdefg';

const hash = crypto.createHmac('sha256', secret)
                   .update('Welcome to JavaTpoint')
                   .digest('hex');

console.log(hash);
```

### Encrypting — Cipher

```js
const crypto = require('crypto');
const cipher = crypto.createCipher('aes192', 'a password');

var encrypted = cipher.update('Hello JavaTpoint', 'utf8', 'hex');
encrypted += cipher.final('hex');

console.log(encrypted);
```

### Decrypting — Decipher

```js
const crypto = require('crypto');
const decipher = crypto.createDecipher('aes192', 'a password');

var decrypted = decipher.update(encrypted, 'hex', 'utf8');
decrypted += decipher.final('utf8');

console.log(decrypted);   // Hello JavaTpoint
```

> **Modern note:** `crypto.createCipher` / `createDecipher` are deprecated in current Node. Today you use `crypto.createCipheriv(algorithm, key, iv)` with an explicit key and initialisation vector. The notes' version still explains the idea correctly: encrypt in chunks with `update()`, then flush the last block with `final()`.

---

## A14. TLS / SSL (page 26–28)

**TLS = Transport Layer Security**, the successor of **SSL (Secure Socket Layer)**. TLS/SSL is a **public-key cryptography** based protocol. It encrypts the connection at the **TCP layer**.

### How public-key cryptography works (page 27)

- Each client and each server has a **public key** and a **private key**.
- The **public key is shared**; the **private key is kept secret**.
- To send an encrypted message you use **your own private key** together with the **recipient's public key**.
- To read a message you decrypt it with **your own private key**.

Load the module with `const tls = require('tls')`.

### Example — `tls_client.js`

```js
const tls = require('tls');

function connected(stream) {
    if (stream) {
        stream.write("GET / HTTP/1.0\n\rHost: encrypted.google.com:443\n\r\n\r");
    } else {
        console.log("Connection failed");
    }
}

var dummy = this;

dummy.socket = tls.connect(443, 'encrypted.google.com', function () {
    dummy.connected = true;
    if (dummy.socket.authorized) {
        dummy.socket.setEncoding('utf-8');
        connected(dummy.socket);
    } else {
        console.log(dummy.socket.authorizationError);
        connected(null);
    }
});

dummy.socket.addListener('data', function (data) {
    console.log(data);
});

dummy.socket.addListener('error', function (error) {
    console.log("FAIL");
    console.log(error);
});

dummy.socket.addListener('close', function () {
    console.log('close');
});
```

`socket.authorized` tells you whether the server's certificate was verified; if not, `authorizationError` says why.

---

## A15. The Debugger (page 29)

Node.js includes a **debugging utility** accessed by a built-in debugging client. The Node.js debugger client is not a full-featured debugger, but simple stepping and inspection are possible. It uses a **TCP based protocol**.

Usage:

```bash
node debug [script.js | -e "script" | <host>:<port>]
```

Example:

```bash
node debug main.js
```

Output starts with:

```
< Debugger listening on port 5858
```

---

## A16. The Process object (page 29–31)

`process` is a **global object**, an instance of **EventEmitter**, that gives information about — and control over — the current Node.js process. It can be accessed from anywhere without `require`.

Typical uses listed in the notes: get process information (pid, architecture, platform, version, release, uptime, CPU usage), **kill** a process, **set uid**, **set groups**, **set umask**.

### Process properties

| Property | Description |
|---|---|
| `process.arch` | The processor architecture: `'arm'`, `'ia32'`, `'x64'` |
| `process.args` | An array containing the command line arguments |
| `process.env` | An object containing the user environment |
| `process.pid` | The PID of the process |
| `process.platform` | `'darwin'`, `'freebsd'`, `'linux'`, `'sunos'`, `'win32'` |
| `process.release` | Metadata for the current node release |
| `process.version` | The Node.js version |
| `process.versions` | The Node.js version **and its dependencies** |

Example:

```js
console.log(`Process Architecture: ${process.arch}`);
console.log(`Process PID: ${process.pid}`);
console.log(`Process Platform: ${process.platform}`);
console.log(`Process Version: ${process.version}`);
```

### Process functions

| Function | Description |
|---|---|
| `process.cwd()` | Returns the path of the current working directory |
| `process.hrtime()` | Returns the current high-resolution real time in a `[seconds, nanoseconds]` array |
| `process.memoryUsage()` | Returns an object having information of memory usage |
| `process.kill(pid[, signal])` | Kills the process of the given pid |
| `process.uptime()` | Returns the Node.js process uptime in seconds |

---

## A17. Child Process (page 31–34)

Node.js provides a `child_process` module which supports spawning child processes, similar to the `popen(3)` system call. There are **three major ways** to create a child process.

### 1. `child_process.exec(command[, options], callback)`

Runs a command **in a console** and **buffers** the output.

**Options:**

| Option | Meaning / default |
|---|---|
| `cwd` | Current working directory of the child process |
| `env` | Environment key-value pairs |
| `encoding` | Default `'utf8'` |
| `shell` | Shell to execute the command with. Default `'/bin/sh'` on UNIX, `'cmd.exe'` on Windows. Uses the `-c` switch on UNIX and `/s /c` on Windows |
| `timeout` | Default `0` |
| `maxBuffer` | Default `200 * 1024` |
| `killSignal` | Default `'SIGTERM'` |
| `uid` | Sets the user identity of the process |
| `gid` | Sets the group identity of the process |

**Callback** receives three arguments: `error`, `stdout`, `stderr`.

```js
const exec = require('child_process').exec;

exec('my.bat', (err, stdout, stderr) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(stdout);
});
```

### 2. `child_process.spawn(command[, args][, options])`

Launches a new process with the given command. It **returns streams** (stdout/stderr), so it is used when the process returns a **large amount of data**.

`support.js`:

```js
console.log("Child Process " + process.argv[2] + " executed.");
```

`master.js`:

```js
const fs = require('fs');
const child_process = require('child_process');

for (var i = 0; i < 3; i++) {
    var workerProcess = child_process.spawn('node', ['support.js', i]);

    workerProcess.stdout.on('data', function (data) {
        console.log('stdout: ' + data);
    });

    workerProcess.stderr.on('data', function (data) {
        console.log('stderr: ' + data);
    });

    workerProcess.on('close', function (code) {
        console.log('child process exited with code ' + code);
    });
}
```

### 3. `child_process.fork(modulePath[, args][, options])`

A **special case of `spawn()`** used to create **Node processes**. It returns an object with a **built-in communication channel** between parent and child, in addition to all the methods of a normal ChildProcess instance.

```js
const child_process = require('child_process');

for (var i = 0; i < 3; i++) {
    var worker_process = child_process.fork("support.js", [i]);

    worker_process.on('close', function (code) {
        console.log('child process exited with code ' + code);
    });
}
```

---

## A18. Buffers (page 34–36)

### Why buffers exist

Pure JavaScript is Unicode friendly but **not nice to binary data**. When dealing with TCP streams or the file system, it is necessary to handle **octet streams**. Node provides a `Buffer` class to store raw data. A buffer is similar to an array of integers, but it corresponds to a **raw memory allocation outside the V8 heap**.

The `Buffer` class is a **global** class — it can be accessed without importing the buffer module.

### Creating buffers — three ways

```js
// 1. Uninitiated buffer of 10 octets
var buf = new Buffer(10);

// 2. From an array
var buf = new Buffer([10, 20, 30, 40, 50]);

// 3. From a string (optional encoding, default 'utf-8')
var buf = new Buffer("Simply Easy Learning", "utf-8");
```

> **Modern note:** `new Buffer(...)` is deprecated today. Use `Buffer.alloc(10)`, `Buffer.from([10,20,30])` and `Buffer.from("text", "utf-8")` instead. The behaviour explained here is unchanged.

### Writing to a buffer

```
buf.write(string[, offset][, length][, encoding])
```

- `string` — the string data to be written to the buffer
- `offset` — index of the buffer to start writing at, default `0`
- `length` — number of bytes to write, default `buffer.length`
- `encoding` — default `'utf8'`

It returns the **number of octets written**.

```js
buf = new Buffer(256);
len = buf.write("Simply Easy Learning");
console.log("Octets written : " + len);
```

### Reading from a buffer

```
buf.toString([encoding][, start][, end])
```

```js
buf = new Buffer(26);
for (var i = 0; i < 26; i++) {
    buf[i] = i + 97;              // 97 is the char code of 'a'
}

console.log(buf.toString('ascii'));        // abcdefghijklmnopqrstuvwxyz
console.log(buf.toString('ascii', 0, 5));  // abcde
console.log(buf.toString('utf8', 0, 5));   // abcde
console.log(buf.toString(undefined, 0, 5));// abcde  (encoding defaults to utf8)
```

---

## A19. Streams (page 37–39)

**Streams are objects that let you read data from a source or write data to a destination in a continuous fashion.**

### The four types of stream

| Type | Purpose |
|---|---|
| **Readable** | Stream which is used for read operations |
| **Writable** | Stream which is used for write operations |
| **Duplex** | Stream which can be used for both read and write operations |
| **Transform** | A type of duplex stream where the output is computed based on the input |

**Each type of stream is an `EventEmitter` instance** and throws several events at different times.

### Commonly used stream events

| Event | Fired when |
|---|---|
| `data` | Data is available to read |
| `end` | There is no more data to read |
| `error` | There is any error receiving or writing data |
| `finish` | All the data has been flushed to the underlying system |

### Reading from a stream — `main.js`

```js
var fs = require("fs");
var data = '';

// Create a readable stream
var readerStream = fs.createReadStream('input.txt');

// Set the encoding to be utf8
readerStream.setEncoding('UTF8');

// Handle stream events --> data, end, and error
readerStream.on('data', function (chunk) {
    data += chunk;
});

readerStream.on('end', function () {
    console.log(data);
});

readerStream.on('error', function (err) {
    console.log(err.stack);
});

console.log("Program Ended");
```

Notice that `"Program Ended"` prints **first** — the stream events fire later, asynchronously.

### Writing to a stream — `main.js`

```js
var fs = require("fs");
var data = 'Simply Easy Learning';

// Create a writable stream
var writerStream = fs.createWriteStream('output.txt');

// Write the data to stream with encoding to be utf8
writerStream.write(data, 'UTF8');

// Mark the end of file
writerStream.end();

// Handle stream events --> finish, and error
writerStream.on('finish', function () {
    console.log("Write completed.");
});

writerStream.on('error', function (err) {
    console.log(err.stack);
});

console.log("Program Ended");
```

---

## A20. The File System (fs) module (page 39–43)

Node implements file I/O using **simple wrappers around standard POSIX functions**. Import it with:

```js
var fs = require("fs");
```

### Synchronous vs asynchronous — the most important idea

**Every method in the fs module has a synchronous and an asynchronous form.**

- **Asynchronous methods** take the **last parameter as a completion function callback**, and the **first parameter of the callback is an error**.
- It is **better to use the asynchronous method** instead of the synchronous one, because the asynchronous method **never blocks the program execution**, whereas the synchronous one does.

### Reading a file — `main.js`

Create `input.txt` with some text, then:

```js
var fs = require("fs");

// Asynchronous read
fs.readFile('input.txt', function (err, data) {
    if (err) {
        return console.error(err);
    }
    console.log("Asynchronous read: " + data.toString());
});

// Synchronous read
var data = fs.readFileSync('input.txt');
console.log("Synchronous read: " + data.toString());

console.log("Program Ended");
```

Output order: the **synchronous** read prints first, then `Program Ended`, then the **asynchronous** read — because the async callback only runs after the current code finishes.

### Opening a file

```
fs.open(path, flags[, mode], callback)
```

**Flags:**

| Flag | Meaning |
|---|---|
| `r` | Open file for reading. **Exception** occurs if the file does not exist |
| `r+` | Open file for reading and writing. Exception occurs if the file does not exist |
| `rs` | Open file for reading in synchronous mode |
| `rs+` | Open file for reading and writing, asking the OS to open it synchronously. Use with caution |
| `w` | Open file for writing. The file is **created** (if it does not exist) or **truncated** (if it exists) |
| `wx` | Like `w` but **fails if the path exists** |
| `w+` | Open file for reading and writing. Created if it does not exist, truncated if it exists |
| `wx+` | Like `w+` but fails if the path exists |
| `a` | Open file for **appending**. The file is created if it does not exist |
| `ax` | Like `a` but fails if the path exists |
| `a+` | Open file for reading and appending. Created if it does not exist |
| `ax+` | Like `a+` but fails if the path exists |

```js
var fs = require("fs");

fs.open('input.txt', 'r+', function (err, fd) {
    if (err) {
        return console.error(err);
    }
    console.log("File opened successfully!");
});
```

### Getting file information — `fs.stat()`

```
fs.stat(path, callback)
```

The callback receives an `fs.Stats` object with these methods:

| Method | True when the file is... |
|---|---|
| `stats.isFile()` | a simple file |
| `stats.isDirectory()` | a directory |
| `stats.isBlockDevice()` | a block device |
| `stats.isCharacterDevice()` | a character device |
| `stats.isSymbolicLink()` | a symbolic link |
| `stats.isFIFO()` | a FIFO |
| `stats.isSocket()` | a socket |

```js
var fs = require("fs");

fs.stat('input.txt', function (err, stats) {
    if (err) {
        return console.error(err);
    }
    console.log(stats);
    console.log("Got file info successfully!");

    console.log("isFile ? " + stats.isFile());
    console.log("isDirectory ? " + stats.isDirectory());
});
```

---

## A21. The Path module (page 44–45)

The Path module is used to **handle and transform file paths**.

```js
var path = require("path");
```

| # | Method | Description |
|---|---|---|
| 1 | `path.normalize(p)` | Normalizes a string path, taking care of `'..'` and `'.'` parts |
| 2 | `path.join([path1][, path2][, ...])` | Joins all arguments together and normalizes the resulting path |
| 3 | `path.resolve([from ...], to)` | Resolves `to` to an absolute path |
| 4 | `path.isAbsolute(path)` | Determines whether `path` is an absolute path |
| 5 | `path.relative(from, to)` | Solves the relative path from `from` to `to` |
| 6 | `path.dirname(p)` | Returns the directory name of a path — similar to the Unix `dirname` command |
| 7 | `path.basename(p[, ext])` | Returns the last portion of a path — similar to the Unix `basename` command |
| 8 | `path.extname(p)` | Returns the extension of the path, from the last `'.'` to the end of the string. Returns an empty string if there is no `'.'` or if it is the first character |
| 9 | `path.parse(pathString)` | Returns an object from a path string |
| 10 | `path.format(pathObject)` | Returns a path string from an object — the opposite of `path.parse` |

Example — `path_example.js`:

```js
var path = require("path");

console.log(path.normalize('/test/test1//2slashes/1slash/tab/..'));
console.log(path.join('/test', 'test1', '2slashes/1slash', 'tab', '..'));
console.log(path.resolve('path_example.js'));
console.log(path.extname('path_example.js'));   // .js
```

---

## A22. StringDecoder (page 46)

The StringDecoder module **decodes a buffer into a string**. It is similar to `buffer.toString()` but provides **extra support for UTF**.

```js
const StringDecoder = require('string_decoder').StringDecoder;
const decoder = new StringDecoder('utf8');
```

**Two methods:**

| Method | Description |
|---|---|
| `decoder.write(buffer)` | Returns the decoded string |
| `decoder.end()` | Returns any trailing bytes that were left in the buffer |

```js
const buf1 = new Buffer('this is a test');
console.log(decoder.write(buf1));       // this is a test

const buf2 = new Buffer('7468697320697320612074c3a97374', 'hex');
console.log(decoder.write(buf2));

const buf3 = Buffer.from([0x62, 0x75, 0x66, 0x66, 0x65, 0x72]);
console.log(decoder.write(buf3));       // buffer
```

---

## A23. Query String module (page 47)

The Query String module is used to **convert a query string into a JSON object and vice versa**.

```js
const querystring = require('querystring');
```

| Method | Description |
|---|---|
| `querystring.parse(str[, sep][, eq][, options])` | Converts a query string into a JSON object |
| `querystring.stringify(obj[, sep][, eq][, options])` | Converts a JSON object into a query string |

```js
const querystring = require('querystring');

console.log(querystring.parse('name=sonoo&company=javatpoint'));
// { name: 'sonoo', company: 'javatpoint' }
```

---

## A24. Zlib — compression and decompression (page 48–49)

Zlib is used to **zip and unzip** files, using **Gzip** and **deflate/inflate**.

```js
const zlib = require('zlib');
```

### Compressing a file — `zlib_example1.js`

```js
const zlib = require('zlib');
const fs = require('fs');

const gzip = zlib.createGzip();
const inp = fs.createReadStream('input.txt');
const out = fs.createWriteStream('input.txt.gz');

inp.pipe(gzip).pipe(out);
```

### Decompressing a file — `zlib_example2.js`

```js
const zlib = require('zlib');
const fs = require('fs');

const unzip = zlib.createUnzip();
const inp = fs.createReadStream('input.txt.gz');
const out = fs.createWriteStream('input2.txt');

inp.pipe(unzip).pipe(out);
```

`pipe()` is the key idea: read stream → transform stream → write stream, with Node handling the chunking for you.

---

## A25. Assertion testing (page 49)

**`assert` is the most elementary way to write tests.** It provides **no feedback when running your test unless one fails**. The module provides a simple set of assertion tests that can be used to test invariants. It is intended for internal use by Node.js but can be used in application code via `require('assert')`. **It is not a testing framework.**

```js
var assert = require('assert');

function add(a, b) {
    return a + b;
}

var expected = add(1, 2);
assert(expected === 3, 'one plus two is three');
```

If the assertion is true, **there is no output at all** — make the test fail on purpose (e.g. `expected === 4`) to see the assertion error.

---

## A26. The V8 module (page 50–52)

**V8** is an open-source JavaScript engine developed by the Chromium project for Google Chrome. It is **written in C++** and is used in Couchbase, MongoDB and Node.js.

The V8 module in Node exposes interfaces specific to the V8 version built into the Node binary:

```js
const v8 = require('v8');
```

### `v8.getHeapStatistics()`

Returns statistics about the V8 heap: total heap size, used heap size, heap size limit and total available size.

Sample output:

```js
{
  total_heap_size: 8304512,
  total_heap_size_executable: 5242880,
  total_physical_size: 8304512,
  total_available_size: 1491075504,
  used_heap_size: 4289960,
  heap_size_limit: 1535115264
}
```

### `v8.getHeapSpaceStatistics()`

Returns an **array of 5 objects**, one per heap space: `new_space`, `old_space`, `code_space`, `map_space`, `large_object_space`. Each object contains `space_name`, `space_size`, `space_used_size`, `space_available_size`, `physical_space_size`.

### Memory limit of V8 in Node.js

- By default: **512 MB on 32-bit** systems and **1 GB on 64-bit** systems.
- The limit can be raised with **`--max-old-space-size`**, up to roughly **1 GB on 32-bit** and **1.7 GB on 64-bit**.
- If you are hitting memory limits, it is **recommended to split your single process into several workers** rather than keep raising the limit.

---

## A27. Callbacks — blocking vs non-blocking (page 52–53)

**A callback is the asynchronous equivalent of a function.** It is called at the completion of a given task. **All the APIs of Node are written in a way that they support callbacks.**

For example, when a function starts reading a file, it **returns control to the execution environment immediately** so that the next instruction can be executed. In Node.js, once the file I/O is complete, the callback function is called with the file contents. So there is **no blocking or waiting** for file I/O — this makes Node.js **highly scalable**, since it can process a high number of requests without waiting for any function to return results.

### Blocking code example

`input.txt`:

```
JavaTpoint is a website for learning technologies.
```

`main.js`:

```js
var fs = require("fs");

var data = fs.readFileSync('input.txt');

console.log(data.toString());
console.log("Program Ended");
```

Output:

```
JavaTpoint is a website for learning technologies.
Program Ended
```

### Non-blocking code example

`main.js`:

```js
var fs = require("fs");

fs.readFile('input.txt', function (err, data) {
    if (err) return console.error(err);
    console.log(data.toString());
});

console.log("Program Ended");
```

Output:

```
Program Ended
JavaTpoint is a website for learning technologies.
```

**This flipped output is the single most important thing to understand about Node.js.** In the blocking version the program waits for the file; in the non-blocking version it carries on and handles the file when it arrives.

---

## A28. Events and event-driven programming (page 54–56)

### Why events

Events and callbacks in Node.js provide **concurrency**. Since Node.js applications are **single threaded** and every API is **asynchronous**, Node uses asynchronous functions to maintain concurrency. Node uses the **Observer pattern**: the Node thread keeps an **event loop**, and after the completion of any task it fires the corresponding event, which signals the event listener function to execute.

### Event-driven programming

As soon as Node starts its server, it simply **initiates its variables, declares functions and then waits for an event to occur**. This is one of the reasons Node.js is fast compared to other similar technologies. In an event-driven application there is generally a **main loop that listens for events, and then triggers a callback function when one of those events is detected**.

The flow:

```
EventEmitters  --->  Events  --->  Event Loop  --->  Event Handlers
```

### The EventEmitter class

```js
// Import events module
var events = require('events');

// Create an eventEmitter object
var eventEmitter = new events.EventEmitter();

// Bind an event with an event handler
eventEmitter.on('eventName', eventHandler);

// Fire the event
eventEmitter.emit('eventName');
```

### Full example — `main.js`

```js
var events = require('events');
var eventEmitter = new events.EventEmitter();

// Create an event handler
var connectHandler = function connected() {
    console.log('connection successful.');

    // Fire the data_received event
    eventEmitter.emit('data_received');
};

// Bind the connection event with the handler
eventEmitter.on('connection', connectHandler);

// Bind the data_received event with an anonymous function
eventEmitter.on('data_received', function () {
    console.log('data received successfully.');
});

// Fire the connection event
eventEmitter.emit('connection');

console.log("Program Ended.");
```

Output:

```
connection successful.
data received successfully.
Program Ended.
```

---

## A29. Punycode (page 56–58)

**Punycode is an encoding syntax which is used to convert a Unicode (UTF-8) string of characters to a basic ASCII string of characters.** Since **host names only understand ASCII characters**, Punycode is used for that conversion. It is used as **Internationalized Domain Name (IDN or IDNA — Internationalizing Domain Names in Applications)**.

Punycode.js is **bundled with Node.js v0.6.2 and later**. To use it with an older version: `npm install punycode`, then `const punycode = require('punycode')`.

| Method | Purpose | Example |
|---|---|---|
| `punycode.decode(string)` | Converts a Punycode string of ASCII symbols to a Unicode string | `punycode.decode('maana-pta')` → `mañana` |
| `punycode.encode(string)` | Converts a Unicode string to a Punycode ASCII string | `punycode.encode('mañana')` → `maana-pta` |
| `punycode.toASCII(domain)` | Converts a Unicode domain name to Punycode — **only the non-ASCII parts are converted** | `punycode.toASCII('mañana.com')` → `xn--maana-pta.com` |
| `punycode.toUnicode(domain)` | Converts a Punycode domain name to Unicode — only the punycoded parts are converted | `punycode.toUnicode('xn--maana-pta.com')` → `mañana.com` |

---

## A30. The TTY module (page 58–60)

The TTY module contains the **`tty.ReadStream`** and **`tty.WriteStream`** classes. In most cases you will not need to use this module directly.

```js
var tty = require('tty');
```

When Node.js is run inside a TTY context:
- **`process.stdin` is a `tty.ReadStream` instance**
- **`process.stdout` is a `tty.WriteStream` instance**

To check whether Node.js is being run in a TTY context:

```bash
node -p -e "Boolean(process.stdout.isTTY)"
```

Output: `true`

### Class `tty.ReadStream`

A subclass of `net.Socket` that represents the **readable portion** of a TTY. Normally the **only instance is `process.stdin`** (and only when `isatty(0)` is true).

| Member | Description |
|---|---|
| `rs.isRaw` | A Boolean, initialized to `false`. It specifies the current "raw" state of the `tty.ReadStream` instance |
| `rs.setRawMode(mode)` | `mode` should be `true` or `false`. This sets the properties of the `tty.ReadStream` to act as a raw device or as a default device. `isRaw` is set to the resulting mode |

### Class `tty.WriteStream`

A subclass of `net.Socket` that represents the **writable portion** of a TTY. Normally the **only instance is `process.stdout`** (and only when `isatty(1)` is true).

**The `resize` event** is fired whenever either of the `columns` or `rows` properties changes:

```js
process.stdout.on('resize', () => {
    console.log('screen size has changed!');
    console.log(`${process.stdout.columns}x${process.stdout.rows}`);
});
```

| Property | Description |
|---|---|
| `ws.columns` | The number of columns the TTY currently has; updated whenever a `resize` event is emitted |
| `ws.rows` | The number of rows the TTY currently has; updated whenever a `resize` event is emitted |

### TTY example — `tty.js`

```js
var tty = require('tty');

process.stdin.setRawMode(true);
process.stdin.resume();

console.log('I am leaving now');

process.stdin.on('keypress', function (char, key) {
    if (key && key.ctrl && key.name === 'c') {
        process.exit();
    }
});
```

---

## A31. Web module — building a web server (page 61–63)

### What is a Web Server

A web server is a **software program which handles the HTTP requests sent by HTTP clients** like web browsers, and returns web pages in response to the clients. Web servers usually respond with **HTML documents** along with images, style sheets and scripts.

### Web application architecture — the four layers

| Layer | Role |
|---|---|
| **Client Layer** | Web browsers, mobile browsers or applications which make the HTTP requests |
| **Server Layer** | The web server which intercepts the requests made by the clients and passes them the response |
| **Business Layer** | The application server utilized by the web server to do the required processing. This layer interacts with the data layer via a database or some external programs |
| **Data Layer** | The database or any source of data |

```
Client (Mobile Browser / Web Browser / Application)
      |
Server (Web Server)
      |
Business Layer (Application Server, File System)
      |
Data Layer (Database, External System)
```

### Creating a web server that serves files — `server.js`

```js
var http = require('http');
var fs = require('fs');
var url = require('url');

// Create a server
http.createServer(function (request, response) {
    // Parse request containing file name
    var pathname = url.parse(request.url).pathname;

    // Print the name of the file for which request is made
    console.log("Request for " + pathname + " received.");

    // Read the requested file content from file system
    fs.readFile(pathname.substr(1), function (err, data) {
        if (err) {
            console.log(err);
            // HTTP Status: 404 : NOT FOUND
            response.writeHead(404, {'Content-Type': 'text/html'});
        } else {
            // HTTP Status: 200 : OK
            response.writeHead(200, {'Content-Type': 'text/html'});

            // Write the content of the file to response body
            response.write(data.toString());
        }

        // Send the response body
        response.end();
    });
}).listen(8081);

console.log("Server running at http://127.0.0.1:8081/");
```

Now create `index.html` **in the same directory as `server.js`**:

```html
<html>
<head>
<title>Sample page</title>
</head>
<body>
Hello World!
</body>
</html>
```

Run `node server.js` and open `http://127.0.0.1:8081/index.html` → **Hello World!**

`pathname.substr(1)` strips the leading `/` so `/index.html` becomes the relative file name `index.html`.

---

## A32. Node.js with MySQL (page 64–75)

The notes create a folder named **`DBexample`** and put each script in it.

### Create a connection — `connection.js`

```js
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "12345"
});

con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
});
```

```bash
node connection.js
# Connected!
```

### Create a database — `javatpoint.js`

The `CREATE DATABASE` statement is used to create a database in MySQL.

```js
con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");

    con.query("CREATE DATABASE javatpoint", function (err, result) {
        if (err) throw err;
        console.log("Database created");
    });
});
```

### Create a table — `employee.js`

The `CREATE TABLE` command creates a table. **You must define the name of the database when you create the connection.**

```js
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "12345",
    database: "javatpoint"       // <-- required for table operations
});

con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");

    var sql = "CREATE TABLE employees (id INT, name VARCHAR(255), age INT(3), city VARCHAR(255))";

    con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Table created");
    });
});
```

### Create a table with a primary key — `employee2.js`

```js
var sql = "CREATE TABLE employee2 (id INT PRIMARY KEY, name VARCHAR(255), age INT(3), city VARCHAR(255))";
```

### Add a column to an existing table

The `ALTER TABLE` statement adds a column to an existing table:

```js
var sql = "ALTER TABLE employee2 ADD COLUMN salary INT(10)";

con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table altered");
});
```

### Insert a single record — `insert.js`

```js
var sql = "INSERT INTO employees (id, name, age, city) VALUES ('1', 'Ajeet kumar', '27', 'Allahabad')";

con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
});
```

Verify in MySQL with `SELECT * FROM employees;`

### Insert multiple records — `insertall.js`

```bash
node insertall.js
# Number of records inserted: 4
```

**The Result Object:** when executing the insert method, a **result object** is returned which contains information about the insertion (for example `affectedRows` and `insertedCount`).

Sample rows after inserting:

```
RowDataPacket { id: 1, name: 'Ajeet Kumar', age: 27, city: 'Allahabad' }
RowDataPacket { id: 2, name: 'Bharat Kumar', age: 25, city: 'Mumbai' }
RowDataPacket { id: 3, name: 'John Cena',   age: 35, city: 'Las Vegas' }
RowDataPacket { id: 4, name: 'Ryan Cook',   age: 15, city: 'CA' }
```

### Update records — `update.js`

```js
var sql = "UPDATE employees SET city = 'Delhi' WHERE city = 'Allahabad'";

con.query(sql, function (err, result) {
    if (err) throw err;
    console.log(result.affectedRows + " record(s) updated");
});
```

Output: `1 record(s) updated`

### Delete records — `delete.js`

```js
var sql = "DELETE FROM employees WHERE city = 'Delhi'";

con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Number of records deleted: " + result.affectedRows);
});
```

Output: `Number of records deleted: 1`

### Select all records — `select.js`

```js
con.query("SELECT * FROM employees", function (err, result) {
    if (err) throw err;
    console.log(result);
});
```

Equivalent SQL: `SELECT * FROM employees;`

### Select a unique record with WHERE — `selectwhere.js`

```js
con.query("SELECT * FROM employees WHERE id = '1'", function (err, result) {
    if (err) throw err;
    console.log(result);
});
```

Output: `RowDataPacket { id: 1, name: 'Ajeet Kumar', age: 27, city: 'Allahabad' }`

### Select with a wildcard — `selectwildcard.js`

```js
con.query("SELECT * FROM employees WHERE city LIKE 'A%'", function (err, result) {
    if (err) throw err;
    console.log(result);
});
```

This retrieves all records where the city **starts with the letter A**.

### Drop a table — `drop.js`

```js
var sql = "DROP TABLE employee2";

con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table deleted");
});
```

---

## A33. Node.js with MongoDB (page 76–83)

MongoDB is a **NoSQL database** which can be used with Node.js to insert and retrieve data.

### Setup

```bash
service mongodb start        # start the MongoDB service
npm install mongodb --save   # install the driver
```

The notes create a folder named **`MongoDatabase`** for these scripts.

### Create a database — `createdatabase.js`

To create a database in MongoDB you **create a Mongo Client** and specify a **connection URL** with the correct IP address and the name of the database.

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/MongoDatabase";

MongoClient.connect(url, function (err, db) {
    if (err) throw err;
    console.log("Database created!");
    db.close();
});
```

### Create a collection — `employees.js`

MongoDB is a NoSQL database, so **data is stored in a collection instead of a table**. The `createCollection` method creates a collection.

```js
MongoClient.connect(url, function (err, db) {
    if (err) throw err;

    db.createCollection("employees", function (err, res) {
        if (err) throw err;
        console.log("Collection is created!");
        db.close();
    });
});
```

### Insert a record — `insert.js`

The **`insertOne`** method inserts a record into a collection. Its **first argument is an object containing the name and value of each field** in the document you want to insert.

```js
var myobj = { name: "Ajeet kumar", age: "28", address: "Delhi" };

db.collection("employees").insertOne(myobj, function (err, res) {
    if (err) throw err;
    console.log("1 record inserted");
    db.close();
});
```

### Insert multiple records — `insertall.js`

The **`insert`** method takes an **array of objects**.

```js
var myobj = [
    { name: "Mahesh sharma", age: "25", address: "Ghaziabad" },
    { name: "Tom Moody",     age: "31", address: "CA" },
    { name: "Zahira Wasim",  age: "19", address: "Islamabad" }
];

db.collection("customers").insert(myobj, function (err, res) {
    if (err) throw err;
    console.log("Number of records inserted: " + res.insertedCount);
    db.close();
});
```

### Select a single record — `select.js`

**`findOne()`** selects a single document from a collection and returns the **first record**.

```js
db.collection("employees").findOne({}, function (err, result) {
    if (err) throw err;
    console.log(result.name);
    db.close();
});
```

### Select multiple records — `selectall.js`

**`find()`** selects all records from a collection.

```js
db.collection("employees").find({}).toArray(function (err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
});
```

Sample data used in the notes:

```
{ _id: ..., name: 'Ajeet Kumar',   age: '28', address: 'Delhi' }
{ _id: ..., name: 'Mahesh Sharma', age: '25', address: 'Ghaziabad' }
{ _id: ..., name: 'Tom Moody',     age: '31', address: 'CA' }
{ _id: ..., name: 'Zahira Wasim',  age: '19', address: 'Islamabad' }
{ _id: ..., name: 'Juck Ross',     age: '45', address: 'London' }
```

### Filter query — `query1.js`

`find()` is also used to **filter the result on a specific parameter** using a query object.

```js
var query = { address: "Delhi" };

db.collection("employees").find(query).toArray(function (err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
});
```

Output: `{ _id: ..., name: 'Ajeet Kumar', age: '28', address: 'Delhi' }`

### Sorting — `sortasc.js`

The **`sort()`** method sorts the result ascending or descending. Its parameter is an object defining the sorting order:

- **Ascending:** `{ name: 1 }`
- **Descending:** `{ name: -1 }`

```js
var mysort = { name: 1 };

db.collection("employees").find().sort(mysort).toArray(function (err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
});
```

Result order: Ajeet Kumar, Juck Ross, Mahesh Sharma, Tom Moody, Zahira Wasim.

**This is where the Node.js notebook ends (page 83).**

---

# PART B — EXPRESS.JS

## B1. What is Express.js (Express page 1)

Express.js is a **fast, assertive, essential and moderate web framework of Node.js**. You can assume it as a **layer built on top of Node.js** that helps manage a **server** and **routes**. It provides a robust set of features to develop **web and mobile applications**.

### Core features

- Designs **single-page, multi-page and hybrid** web applications.
- Allows you to **set up middlewares** to respond to HTTP requests.
- **Defines a routing table** which is used to perform different actions based on the **HTTP method and URL**.
- Allows you to **dynamically render HTML pages** based on passing arguments to templates.

### Why use Express.js

- **Ultra fast I/O**
- **Asynchronous and single threaded**
- **MVC-like structure**
- **Robust API** makes routing easy

### The smallest possible Express app — `basic_express.js`

```js
var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.send('Welcome to JavaTpoint');
});

var server = app.listen(8000, function () {
    var host = server.address().address;
    var port = server.address().port;
    console.log('Example app listening at http://%s:%s', host, port);
});
```

```bash
node basic_express.js
# Example app listening at http://:::8000
```

Open `127.0.0.1:8000` → **Welcome to JavaTpoint!**

Compare this with the raw `http` server in section A2 — Express removes almost all the boilerplate.

---

## B2. Installing Express.js (Express pages 2–5)

### Global install

```bash
npm install -g express
```

### Local install (into your project)

```bash
npm install express --save
```

This installs Express into your project's `node_modules` folder. `--save` records it in `package.json`.

### Other important modules to install alongside Express

| Module | What it does | Command |
|---|---|---|
| **body-parser** | Node.js middleware for handling **JSON, Raw, Text and URL encoded** form data | `npm install body-parser --save` |
| **cookie-parser** | Parses the **Cookie header** and populates `req.cookies` with an object keyed by cookie names | `npm install cookie-parser --save` |
| **multer** | Node.js middleware for handling **multipart/form-data** (file uploads) | `npm install multer --save` |

### Express.js app example (page 5)

A simple app which starts a server and listens on a local port. It **responds only to the homepage**; **every other path returns 404 Not Found**.

```js
var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.send('Welcome to JavaTpoint');
});

var server = app.listen(8000, function () {
    var host = server.address().address;
    var port = server.address().port;
    console.log('Example app listening at http://%s:%s', host, port);
});
```

---

## B3. The Request object (Express pages 6–10)

**Request and Response objects are the parameters of the callback function** used in Express applications.

```js
app.get('/', function (req, res) {
    // req = request, res = response
});
```

The **request object represents the HTTP request** and has properties for the request **query string, parameters, body, HTTP headers**, and so on.

### Request object properties

| # | Property | Description |
|---|---|---|
| 1 | `req.app` | Holds a reference to the instance of the Express application that is using the middleware |
| 2 | `req.baseurl` | The URL path on which a router instance was mounted |
| 3 | `req.body` | Key-value pairs of data submitted in the request body. **By default it is `undefined`** and is populated when you use **body-parsing middleware** such as `body-parser` |
| 4 | `req.cookies` | When using **cookie-parser** middleware, this property is an object that contains cookies sent by the request |
| 5 | `req.fresh` | Indicates that the request is "fresh"; it is the opposite of `req.stale` |
| 6 | `req.hostname` | Contains the hostname from the "host" HTTP header |
| 7 | `req.ip` | The remote IP address of the request |
| 8 | `req.ips` | When `trust proxy` is `true`, contains an array of IP addresses specified in the "X-Forwarded-For" request header |
| 9 | `req.originalurl` | Much like `req.url`, but it **retains the original request URL**, allowing you to rewrite `req.url` freely for internal routing purposes |
| 10 | `req.params` | An object containing properties mapped to the **named route parameters**. For example, for the route `/user/:name`, the name property is available as `req.params.name`. Defaults to `{}` |
| 11 | `req.path` | Contains the path part of the request URL |
| 12 | `req.protocol` | The request protocol string — `"http"`, or `"https"` when requested with TLS |
| 13 | `req.query` | An object containing a property for **each query string parameter** in the route |
| 14 | `req.route` | The currently-matched route, a string |
| 15 | `req.secure` | A Boolean that is `true` if a **TLS connection** is established |
| 16 | `req.signedCookies` | When using cookie-parser, contains **signed cookies** sent by the request, unsigned and ready for use |
| 17 | `req.stale` | Indicates whether the request is "stale"; the opposite of `req.fresh` |
| 18 | `req.subdomains` | An array of subdomains in the domain name of the request |
| 19 | `req.xhr` | A Boolean that is `true` if the request's `X-Requested-With` header field is `"XMLHttpRequest"`, indicating that the request was issued by a client library such as **jQuery** |

### Request object methods

**`req.accepts(types)`** — checks whether the specified content types are acceptable, based on the request's `Accept` HTTP header field.

```js
req.accepts('html');        // => "html"
req.accepts('text/html');   // => "text/html"
```

**`req.get(field)`** — returns the specified HTTP request header field (case-insensitive).

```js
req.get('Content-Type');    // => "text/plain"
req.get('content-type');    // => "text/plain"
req.get('Something');       // => undefined
```

**`req.is(type)`** — returns `true` if the incoming request's `Content-Type` HTTP header field matches the MIME type specified by the `type` parameter.

```js
// With Content-Type: text/html; charset=utf-8
req.is('html');        // => true
req.is('text/html');   // => true
req.is('text/*');      // => true
```

**`req.param(name[, defaultValue])`** — fetches the value of a param when it is present.

```js
// ?name=sasha
req.param('name');            // => "sasha"

// POST name=sasha
req.param('name');            // => "sasha"

// /user/sasha for the route /user/:name
req.param('name');            // => "sasha"
```

---

## B4. The Response object (Express pages 10–18)

The **Response object (`res`)** specifies the HTTP response which is sent by an Express app when it gets an HTTP request.

**What it does:**
- Sends the response back to the client browser.
- Lets you put new **cookie values** which will be written to the client browser (under the cross-domain rule).
- **Once you call `res.send()` or `res.redirect()` or `res.render()`, you cannot do it again**, otherwise there will be an uncaught error.

### Response object properties

| # | Property | Description |
|---|---|---|
| 1 | `res.app` | Holds a reference to the instance of the Express application that is using the middleware |
| 2 | `res.headersSent` | A Boolean indicating if the app sent HTTP headers for the response |
| 3 | `res.locals` | An object that contains response local variables scoped to the request |

### Response object methods

**`res.append(field[, value])`** — appends the specified value to the HTTP response header field.

```js
res.append('Link', ['<http://localhost/>', '<http://localhost:3000/>']);
res.append('Warning', '199 Miscellaneous Warning');
```

**`res.attachment([filename])`** — sends a file as an attachment in the HTTP response.

```js
res.attachment('path/to/js_pic.png');
```

**`res.cookie(name, value[, options])`** — sets a cookie name to a value. The value can be a string or an object converted to JSON.

```js
res.cookie('name', 'Aryan', { domain: 'xyz.com', path: '/admin', secure: true });
res.cookie('Section', { Names: ['Aryan', 'Sushil', 'Priyanka'] });
res.cookie('Cart', { items: [1, 2, 3] }, { maxAge: 900000 });
```

**`res.clearCookie(name[, options])`** — clears the cookie specified by name.

```js
res.cookie('name', 'Aryan', { path: '/admin' });   // set
res.clearCookie('name', { path: '/admin' });       // clear
```

**`res.download(path[, filename][, fn])`** — transfers the file at path as an "attachment" and **forces the browser to prompt the user for download**.

```js
res.download('/report-12345.pdf');
```

**`res.end([data][, encoding])`** — ends the response process.

```js
res.end();
res.status(404).end();
```

**`res.format(object)`** — performs **content negotiation** on the `Accept` HTTP header of the request object, when present.

```js
res.format({
    'text/plain': function () { res.send('hey'); },
    'text/html':  function () { res.send('<p>hey</p>'); },
    'application/json': function () { res.send({ message: 'hey' }); },
    default: function () { res.status(406).send('Not Acceptable'); }
});
```

**`res.get(field)`** — provides the HTTP response header specified by field.

```js
res.get('Content-Type');
```

**`res.json([body])`** — returns the response in **JSON format**.

```js
res.json(null);
res.json({ name: 'ajeet' });
```

**`res.jsonp([body])`** — returns the response in JSON format **with JSONP support**.

```js
res.jsonp(null);
res.jsonp({ name: 'ajeet' });
```

**`res.links(links)`** — populates the response's `Link` HTTP header field by joining the links provided as properties of the parameter.

```js
res.links({
    next: 'http://api.rnd.com/users?page=5',
    last: 'http://api.rnd.com/users?page=10'
});
```

**`res.location(path)`** — sets the response `Location` HTTP header field based on the specified path parameter.

```js
res.location('http://xyz.com');
```

**`res.redirect([status,] path)`** — redirects to the URL derived from the specified path, with the specified HTTP status.

```js
res.redirect('http://example.com');
```

**`res.render(view[, locals][, callback])`** — renders a view and **sends the rendered HTML string** to the client.

```js
// send the rendered view to the client
res.render('index');

// pass a local variable to the view
res.render('user', { name: 'aryan' }, function (err, html) {
    // ...
});
```

**`res.send([body])`** — sends the HTTP response.

```js
res.send(new Buffer('whoop'));
res.send({ some: 'json' });
res.send('<p>some html</p>');
```

**`res.sendFile(path[, options][, fn])`** — transfers the file at the given path. It **sets the `Content-Type` response HTTP header field based on the filename's extension**.

```js
res.sendFile(fileName, options, function (err) {
    // ...
});
```

**`res.set(field[, value])`** — sets the response HTTP header field to a value.

```js
res.set('Content-Type', 'text/plain');

res.set({
    'Content-Type': 'text/plain',
    'Content-Length': '123'
});
```

**`res.status(code)`** — sets an HTTP status for the response.

```js
res.status(403).end();
res.status(400).send('Bad Request');
```

**`res.type(type)`** — sets the `Content-Type` HTTP header to the MIME type.

```js
res.type('.html');            // => 'text/html'
res.type('html');             // => 'text/html'
res.type('json');             // => 'application/json'
res.type('application/json'); // => 'application/json'
res.type('png');              // => image/png
```

---

## B5. GET requests (Express pages 18–24)

**GET and POST are the two common HTTP requests used for building REST APIs.**

- **GET requests** are used to send only a **limited amount of data** because the data is sent **in the header**.
- **POST requests** are used to send a **large amount of data** because the data is sent **in the body**.

Express.js facilitates you to handle GET and POST requests using the instance of express.

### GET Method Example 1 — fetch data in JSON format

The GET method sends only a limited amount of data because data is sent in the header. **It is not secure because the data is visible in the URL bar.**

`index.html`:

```html
<html>
<body>
<form action="http://127.0.0.1:8081/process_get" method="GET">
First Name: <input type="text" name="first_name"><br>
Last Name: <input type="text" name="last_name">
<input type="submit" value="Submit">
</form>
</body>
</html>
```

`get_example1.js`:

```js
var express = require('express');
var app = express();

app.use(express.static('public'));

app.get('/index.html', function (req, res) {
    res.sendFile(__dirname + "/" + "index.html");
});

app.get('/process_get', function (req, res) {
    // Prepare output in JSON format
    response = {
        first_name: req.query.first_name,
        last_name:  req.query.last_name
    };
    console.log(response);
    res.end(JSON.stringify(response));
});

var server = app.listen(8000, function () {
    var host = server.address().address;
    var port = server.address().port;
    console.log("Example app listening at http://%s:%s", host, port);
});
```

Fill in "Ajeet" and "Kumar" and submit. The browser goes to
`127.0.0.1:8000/process_get?first_name=Ajeet&last_name=Kumar` and shows:

```json
{"first_name":"Ajeet","last_name":"Kumar"}
```

**Key point:** GET data arrives in **`req.query`**.

### GET Method Example 2 — fetch data in paragraph format

`index.html` form posts to `http://127.0.0.1:8000/get_example2` with method `GET`.

`get_example2.js`:

```js
var express = require('express');
var app = express();

app.get('/get_example2', function (req, res) {
    res.send('<p>Username: ' + req.query['first_name'] + '</p>' +
             '<p>Lastname: ' + req.query['last_name'] + '</p>');
});

var server = app.listen(8000, function () { /* ... */ });
```

Fill "Rahul" / "Kumar" → the page shows **Username: Rahul** and **Lastname: Kumar**.

### GET Method Example 3 — a bigger form

`index.html`:

```html
<!DOCTYPE html>
<html>
<body>
<form action="http://127.0.0.1:8000/get_example3">
<table>
<tr><td>Enter First Name:</td><td><input type="text" name="firstname"/></td></tr>
<tr><td>Enter Last Name:</td><td><input type="text" name="lastname"/></td></tr>
<tr><td>Enter Password:</td><td><input type="password" name="password"/></td></tr>
<tr><td>Sex:</td><td>
  <input type="radio" name="sex" value="male">Male
  <input type="radio" name="sex" value="female">Female
</td></tr>
<tr><td>About You:</td><td>
  <textarea rows="5" cols="40" name="aboutyou" placeholder="Write about yourself"></textarea>
</td></tr>
<tr><td colspan="2"><input type="submit" value="register"/><br/></td></tr>
</table>
</form>
</body>
</html>
```

`get_example3.js`:

```js
var express = require('express');
var app = express();

app.get('/get_example3', function (req, res) {
    res.send('<p>Firstname: ' + req.query['firstname'] + '</p>' +
             '<p>Lastname: '  + req.query['lastname']  + '</p>' +
             '<p>Password: '  + req.query['password']  + '</p>' +
             '<p>AboutYou: '  + req.query['aboutyou']  + '</p>');
});

var server = app.listen(8000, function () { /* ... */ });
```

Output for John / Alex / alexender / "Hi.. My name is John. I live in the beautiful city of Paris.":

```
Firstname  John
Lastname   Alex
Password   alexender
AboutYou   Hi.. My name is John. I live in the beautiful city of Paris.
```

Notice the password is visible in the URL — this is exactly why GET is described as *not secure*.

---

## B6. POST requests (Express pages 24–26)

**The POST method** facilitates you to send a large amount of data because **the data is sent in the body**. POST is **secure because the data is not visible in the URL bar**, but **it is not used as popularly as the GET method**. On the other hand, the **GET method is more efficient and used more than POST**.

### POST Example 1 — fetch data in JSON format

`index.html`:

```html
<html>
<body>
<form action="http://127.0.0.1:8000/process_post" method="POST">
First Name: <input type="text" name="first_name"><br>
Last Name:  <input type="text" name="last_name">
<input type="submit" value="Submit">
</form>
</body>
</html>
```

`post_example1.js`:

```js
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

// Create application/x-www-form-urlencoded parser
var urlencodedParser = bodyParser.urlencoded({ extended: false });

app.use(express.static('public'));

app.get('/index.html', function (req, res) {
    res.sendFile(__dirname + "/" + "index.html");
});

app.post('/process_post', urlencodedParser, function (req, res) {
    // Prepare output in JSON format
    response = {
        first_name: req.body.first_name,
        last_name:  req.body.last_name
    };
    console.log(response);
    res.end(JSON.stringify(response));
});

var server = app.listen(8000, function () { /* ... */ });
```

Fill "Mohan" / "Bhargav" and submit → you get the data in JSON format:

```json
{"first_name":"Mohan","last_name":"Bhargav"}
```

**Key point:** POST data arrives in **`req.body`**, and `req.body` only works because `urlencodedParser` (body-parser) was added as middleware for this route.

---

## B7. Routing (Express pages 27–29)

**Routing** is made from the word *route*. It is used to **determine the specific behaviour of an application**. It specifies **how an application responds to a client request to a particular route, URI or path, and a specific HTTP request method (GET, POST etc.)**. It can handle different types of HTTP requests.

### Example — `routing_example.js`

```js
var express = require('express');
var app = express();

// This responds a GET request for the homepage
app.get('/', function (req, res) {
    console.log("Got a GET request for the homepage");
    res.send('Welcome to JavaTpoint!');
});

// This responds a POST request for the homepage
app.post('/', function (req, res) {
    console.log("Got a POST request for the homepage");
    res.send('I am Impossible');
});

// This responds a DELETE request for /del_student
app.delete('/del_student', function (req, res) {
    console.log("Got a DELETE request for /del_student");
    res.send('I am deleted!');
});

// This responds a GET request for /enrolled_student
app.get('/enrolled_student', function (req, res) {
    console.log("Got a GET request for /enrolled_student");
    res.send('I am an enrolled student.');
});

// This responds a GET request for abcd, abxcd, ab123cd, and so on
app.get('/ab*cd', function (req, res) {
    console.log("Got a GET request for /ab*cd");
    res.send('Pattern Matched');
});

var server = app.listen(8000, function () { /* ... */ });
```

Run it and visit:
- `http://127.0.0.1:8000` → **Welcome to JavaTpoint!**
- `http://127.0.0.1:8000/enrolled_student` → **I am an enrolled student**

**Note:** the command prompt will be updated after one successful response — each request logs a line.

The `'/ab*cd'` route shows **pattern matching**: it matches `abcd`, `abxcd`, `ab123cd` and so on.

---

## B8. Cookies management (Express pages 29–32)

### What are cookies

**Cookies are small pieces of information which are sent from a website and stored in the user's web browser when the user browses that website.** Every time the user loads that website back, the browser sends that stored data back to the website or server, to **recognize the user**.

```
Browser  --1) Request-------------->  Server
Browser  <--2) Response + Cookie----  Server
Browser  --3) Request + Cookie----->  Server
```

### Install cookie-parser

You have to acquire cookies abilities in Express.js, so install the **cookie-parser** middleware through npm:

```bash
npm install cookie-parser
```

### Import cookie-parser into your app

```js
var express = require('express');
var cookieParser = require('cookie-parser');
var app = express();

app.use(cookieParser());
```

### Define a route

Cookie-parser **parses the Cookie header and populates `req.cookies`** with an object keyed by the cookie names.

```js
// set a new cookie
app.get('/cookie', function (req, res) {
    res.cookie('cookie_name', 'cookie_value').send('Cookie is set');
});

// read cookies
app.get('/', function (req, res) {
    console.log("Cookies: ", req.cookies);
});
```

**The browser sends back that cookie to the server every time it requests that website.**

### Full example — `cookies_example.js`

```js
var express = require('express');
var cookieParser = require('cookie-parser');
var app = express();

app.use(cookieParser());

app.get('/cookieset', function (req, res) {
    res.cookie('cookie_name', 'cookie_value');
    res.cookie('Company', 'javatpoint');
    res.cookie('name', 'sonoo');
    res.status(200).send('cookie is set');
});

app.get('/', function (req, res) {
    res.status(200).send('Welcome to JavaTpoint');
});

var server = app.listen(8000, function () { /* ... */ });
```

Output:
- `http://127.0.0.1:8000/` → **Welcome to JavaTpoint!**
- `http://127.0.0.1:8000/cookieset` → **Cookie is set**
- `http://127.0.0.1:8000/cookieget` → `{"cookie_name":"cookie_value","company":"javatpoint","name":"sonoo"}`

---

## B9. File upload (Express pages 32–37)

In Express.js, **file upload is slightly difficult because of its asynchronous nature and networking approach**. It can be done by **using middleware to handle multipart/form data**. There are many middlewares that can be used, like **multer, connect, body-parser** etc. This example uses **multer**.

### Project structure

Create a folder **"jtp file upload"** containing:

| Item | Purpose |
|---|---|
| `uploads/` | An **empty folder** created to store the uploaded images |
| `index.html` | The upload form |
| `package.json` | Dependencies |
| `server.js` | The Express server |

### `package.json`

```json
{
  "name": "file_upload",
  "version": "0.0.1",
  "dependencies": {
    "express": "4.13.3",
    "multer": "1.1.0"
  },
  "devDependencies": {
    "should": "~7.1.0",
    "mocha": "~2.3.3",
    "supertest": "~1.1.0"
  }
}
```

### `index.html`

```html
<html>
<head>
<title>File upload in Node.js by Javatpoint</title>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery.form/3.51/jquery.form.min.js"></script>
<script>
$(document).ready(function () {
    $('#uploadForm').submit(function () {
        $("#status").empty().text("File is uploading...");

        $(this).ajaxSubmit({
            error: function (xhr) {
                status('Error: ' + xhr.status);
            },
            success: function (response) {
                console.log(response);
                $("#status").empty().text(response);
            }
        });

        return false;
    });
});
</script>
</head>
<body>
<h1>Express.js File upload: by Javatpoint</h1>
<form id="uploadForm" enctype="multipart/form-data" action="/uploadjavatpoint" method="post">
<input type="file" name="myfile"/><br/><br/>
<input type="submit" value="Upload Image" name="submit"><br/><br/>
<span id="status"></span>
</form>
</body>
</html>
```

### `server.js`

```js
var express = require("express");
var multer  = require('multer');
var app = express();

var storage = multer.diskStorage({
    destination: function (req, file, callback) {
        callback(null, './uploads');
    },
    filename: function (req, file, callback) {
        callback(null, file.originalname);
    }
});

var upload = multer({ storage: storage }).single('myfile');

app.get('/', function (req, res) {
    res.sendFile(__dirname + "/index.html");
});

app.post('/uploadjavatpoint', function (req, res) {
    upload(req, res, function (err) {
        if (err) {
            return res.end("Error uploading file");
        }
        res.send("File is uploaded successfully!");
    });
});

app.listen(2000, function () {
    console.log("Server is running on port 2000");
});
```

### Run it

```bash
npm install        # creates node_modules inside "jtp file upload"
node server.js     # Server is running on port 2000
```

Open `http://127.0.0.1:2000/`, choose an image, click **Upload Image** →
**"File is uploaded successfully!"** and the file (e.g. `Tulips.jpg`) appears in the **`uploads`** folder.

---

## B10. Middleware (Express pages 37–42)

### What middleware is

**Express.js middleware are different types of functions that are invoked by the Express.js routing layer before the final request handler.** As the name specifies, **middleware appears in the middle between an initial request and the final intended route**. In a stack, **middleware functions are always invoked in the order in which they are added**.

Middleware is commonly used to perform tasks like **body parsing** for URL-encoded or JSON requests, **cookie parsing** for basic cookie handling, or even **building JavaScript modules on the fly**.

### What is a middleware function

**Middleware functions are the functions that have access to the request and response object (`req`, `res`) in the request-response cycle.** A middleware function can perform the following tasks:

- It can **execute any code**.
- It can **make changes to the request and the response objects**.
- It can **end the request-response cycle**.
- It can **call the next middleware function** in the stack.

### The five types of middleware in an Express.js app

1. **Application-level middleware**
2. **Router-level middleware**
3. **Error-handling middleware**
4. **Built-in middleware**
5. **Third-party middleware**

### Step 1 — a basic app with no middleware (`simple_express.js`)

```js
var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.send('Welcome to JavaTpoint');
});

app.get('/help', function (req, res) {
    res.send('How can I help you?');
});

var server = app.listen(8000, function () { /* ... */ });
```

Visit `http://127.0.0.1:8000` and `http://127.0.0.1:8000/help`.

**Note:** the command prompt is **not changed** — it is **not showing any record of the GET request**, although a GET request is processed on the `/help` page.

### Step 2 — adding middleware (`simple_middleware.js`)

**If you want to record every time you get a request, then you can use a middleware.**

```js
var express = require('express');
var app = express();

app.use(function (req, res, next) {
    console.log('%s %s', req.method, req.url);
    next();
});

app.get('/', function (req, res, next) {
    res.send('Welcome to JavaTpoint');
});

app.get('/help', function (req, res, next) {
    res.send('How can I help you?');
});

var server = app.listen(8000, function () { /* ... */ });
```

Now the browser output is the same, but **the command prompt displays a GET result**:

```
GET /
GET /help
```

**As many times as you reload the page, the command prompt will be updated.**

**Note:** in the above example the **`next()`** middleware is used.

### Middleware example explanation

- In the above middleware example a **new function is used to invoke with every request via `app.use()`**.
- **Middleware is a function, just like route handlers, and is invoked in a similar manner.**
- **You can add more middlewares above or below using the same API.**

The critical rule for a beginner: **if your middleware does not call `next()` (and does not end the response), the request hangs forever.**

---

## B11. Scaffolding (Express pages 42–45)

### What is scaffolding

**Scaffolding is a technique that is supported by some MVC frameworks.** It is mainly supported by the following frameworks: **Ruby on Rails, OutSystem Platform, Express Framework, Play framework, Django, MonoRail, Brail, Symfony, Laravel, CodeIgniter, Yii, CakePHP, Phalcon PHP, Model-Glue, PRADO, Grails, Catalyst, Seam Framework, Spring ROO, ASP.NET** etc.

**Scaffolding facilitates the programmers to specify how the application data may be used.** This specification is used by the frameworks, with **predefined code templates**, to generate the final code that the application can use for **CRUD operations (create, read, update and delete database entries)**.

### Express.js Scaffold

An Express.js scaffold supports **Candy** and more web projects based on Node.js.

### Install scaffold

```bash
npm install express-scaffold
```

It will take a few seconds. After this step, execute the following command to install the **express generator**:

```bash
npm install -g express-generator
```

Now you can use express to scaffold a web-app.

### Example

First create a directory named **`myapp`**. Create a file named **`app.js`** in the `myapp` directory with the following code:

```js
var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.send('Welcome to JavaTpoint');
});

app.listen(8000, function () {
    console.log('Example app listening on port 8000!');
});
```

Open the Node.js command prompt, go to `myapp` and run:

```bash
npm init
```

`npm init` walks you through creating a `package.json` file. It only covers the most common items and tries to guess sensible defaults. **Fill the entries and press enter.**

It will create a **`package.json`** file in the `myapp` folder, and the data is shown in JSON format:

```json
{
  "name": "myapp",
  "version": "1.0.0",
  "description": "This is my first app.",
  "main": "myapp.js",
  "scripts": { "test": "No" },
  "author": "Sonoo",
  "license": "ISC"
}
```

---

## B12. Template engines and Pug (Express pages 47–50)

*(The scan skips handwritten page 46; the topic continues here.)*

### Using template engines with Express

**A template engine makes you able to use a static template file in your application.** To render template files you have to set the following application setting properties:

| Property | Meaning | Example |
|---|---|---|
| **views** | Specifies a directory where the template files are located | `app.set('views', './views')` |
| **view engine** | Specifies the template engine that you use | `app.set('view engine', 'pug')` |

### Pug template engine

**Pug** (formerly known as **jade**) is a template engine for Node.js. **Pug uses whitespaces and indentation as part of the syntax.** Its syntax is easy to learn.

### Install pug

```bash
npm install pug --save
```

**Pug templates must be written inside a `.pug` file, and all `.pug` files must be put inside the `views` folder in the root folder of the Node.js application.**

**Note:** by default Express.js searches all the views in the **`views` folder under the root folder**. You can also set another folder using the `views` property in express, for example:

```js
app.set('views', 'myviews');
```

### How Pug renders HTML

The pug template engine takes the input in a simple way and produces the output in HTML.

**Simple input (`index.pug`):**

```pug
doctype html
html
  head
    title A simple pug example
  body
    h1 This page is produced by pug template engine
    p Some paragraph here..
```

**Output produced by the pug template:**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>A simple pug example</title>
  </head>
  <body>
    <h1>This page is produced by pug template engine</h1>
    <p>Some paragraph here..</p>
  </body>
</html>
```

Notice there are **no closing tags** in Pug — indentation defines the nesting.

### Rendering a Pug view from Express — `server.js`

```js
var express = require('express');
var app = express();

// set view engine
app.set("view engine", "pug");

app.get('/', function (req, res) {
    res.render('index');
});

var server = app.listen(5000, function () {
    console.log('Node server is running..');
});
```

Create `index.pug` inside the `views` folder with the template shown above, run `node server.js`, and open port 5000 — Express finds `views/index.pug`, renders it to HTML and sends it to the browser.

**Express.js can be used with any template engine** — pug is just the one demonstrated here.

**This is where the Express.js notebook ends (page 50).**

---

# PART C — INTERVIEW QUESTIONS

> **Source note:** none of the six PDFs contained an interview-question section. The questions below are derived **only** from the material transcribed in Parts A and B, so every answer is backed by the notes. They are ordered easy → hard.

### Basics

**1. What is Node.js?**
An open-source, cross-platform runtime environment for server-side and networking applications, written in JavaScript. Node.js = JavaScript runtime environment + JavaScript library. It runs on OS X, Windows and Linux.

**2. Which engine does Node.js use, and why does it matter?**
Google Chrome's **V8** engine, written in C++. It is why Node code execution is extremely fast. V8 is also used by MongoDB and Couchbase.

**3. Is Node.js single threaded or multi threaded?**
Single threaded, with **event looping**. Because every API is asynchronous and events deliver the results, one thread can serve far more concurrent requests than a traditional thread-per-request server such as Apache HTTP Server.

**4. What license is Node.js released under?**
The **MIT license**.

**5. What does "no buffering" mean in Node.js?**
Node.js applications never buffer any data; they simply **output the data in chunks**.

### Modules and tooling

**6. What are the two functionalities of npm?**
(1) Online repositories for Node.js packages/modules, searchable at `search.nodejs.org`; (2) a command line utility to install packages and do version and dependency management. npm has been bundled with Node since **v0.6.3**.

**7. How do you install, uninstall and search for a module?**
`npm install <name>`, `npm uninstall <name>`, `npm search <name>`. Add `--save` to record the dependency in `package.json`, `-g` to install globally.

**8. What does REPL stand for and what are its four steps?**
**Read, Eval, Print, Loop.** Read the input and parse it into a data structure in memory; evaluate the data structure; print the result; loop until the user presses `Ctrl+C` twice.

**9. In the REPL, why does `var x = 10` print `undefined` while `x = 10` prints `10`?**
A `var` declaration is a statement with no value, so it evaluates to `undefined`. A bare assignment is an expression whose value is the assigned value.

**10. What does `_` do in the REPL?**
It holds the result of the **last** evaluated expression.

### Globals, OS, process

**11. What is the difference between `__dirname` and `__filename`?**
`__dirname` is the directory of the currently executing script; `__filename` is the absolute path of the file, including the filename. Both are global — no `require` needed.

**12. Name five things `os` can tell you.**
Any five of: `os.arch()`, `os.cpus()`, `os.endianness()`, `os.freemem()`, `os.totalmem()`, `os.homedir()`, `os.hostname()`, `os.loadavg()`, `os.networkInterfaces()`, `os.platform()`, `os.release()`, `os.tmpdir()`, `os.type()`, `os.uptime()`, `os.userInfo()`.

**13. What is `process` and what class does it extend?**
A **global object** giving information about and control over the current process. It is an instance of **EventEmitter**. Key properties: `arch`, `args`, `env`, `pid`, `platform`, `release`, `version`, `versions`. Key functions: `cwd()`, `hrtime()`, `memoryUsage()`, `kill(pid[,signal])`, `uptime()`.

### Async model — the core of Node

**14. What is a callback?**
The asynchronous equivalent of a function, called at the completion of a given task. All Node APIs support callbacks. When a function starts reading a file it returns control to the execution environment immediately, so the next instruction runs; the callback fires later with the result.

**15. Show the difference between blocking and non-blocking code and explain the output.**
`fs.readFileSync` prints the file contents **then** "Program Ended". `fs.readFile` with a callback prints "Program Ended" **first**, then the file contents — because the callback runs only after the current code finishes.

**16. In an asynchronous fs method, where does the callback go and what is its first parameter?**
The callback is the **last parameter**, and its **first parameter is an error**.

**17. Which design pattern does Node use for events, and what is the event flow?**
The **Observer pattern**. Flow: **EventEmitters → Events → Event Loop → Event Handlers**.

**18. How do you bind and fire a custom event?**
```js
var events = require('events');
var eventEmitter = new events.EventEmitter();
eventEmitter.on('eventName', handler);   // bind
eventEmitter.emit('eventName');          // fire
```

**19. What is event-driven programming in Node?**
As soon as Node starts its server it initiates variables, declares functions, and then **waits for an event to occur**. A main loop listens for events and triggers a callback when one is detected. This is one of the reasons Node is fast.

### Buffers, streams, files

**20. Why does Node need Buffers?**
Pure JavaScript is Unicode friendly but not good with binary data. When handling TCP streams or the file system you must handle octet streams, so Node provides `Buffer`, a raw memory allocation **outside the V8 heap**, similar to an array of integers. `Buffer` is global.

**21. What are the four types of stream?**
**Readable** (read), **Writable** (write), **Duplex** (both), **Transform** (a duplex stream whose output is computed from its input). Every stream is an `EventEmitter`.

**22. Name the four common stream events.**
`data` (data available to read), `end` (no more data), `error` (error while reading or writing), `finish` (all data flushed to the underlying system).

**23. What is the difference between the `w`, `wx`, `a` and `ax` file flags?**
`w` creates or truncates for writing; `wx` is the same but **fails if the path exists**; `a` opens for appending and creates the file if it does not exist; `ax` is the same but fails if the path exists.

**24. How do you find out whether a path is a file or a directory?**
`fs.stat(path, callback)`; the callback's `stats` object has `isFile()`, `isDirectory()`, `isBlockDevice()`, `isCharacterDevice()`, `isSymbolicLink()`, `isFIFO()`, `isSocket()`.

**25. What does `path.extname()` return when there is no dot?**
An empty string — and also when the dot is the first character of the basename.

### Processes and performance

**26. What are the three ways to create a child process, and when do you use each?**
`exec` runs a command in a console and **buffers** the output (small outputs); `spawn` returns **streams** and is used when the process returns a **large amount of data**; `fork` is a special case of `spawn` for creating **Node processes**, with a built-in communication channel to the parent.

**27. What is the default V8 memory limit in Node and how do you change it?**
About **512 MB on 32-bit** and **1 GB on 64-bit**. Raise it with **`--max-old-space-size`** up to roughly 1 GB (32-bit) / 1.7 GB (64-bit). If you are hitting the limit, the recommended fix is to **split the single process into several workers**.

**28. Which two functions does the `v8` module provide?**
`v8.getHeapStatistics()` (total heap size, used heap size, heap size limit, total available size) and `v8.getHeapSpaceStatistics()` (an array of 5 objects: `new_space`, `old_space`, `code_space`, `map_space`, `large_object_space`).

### Security and encoding

**29. What is the difference between a hash and an HMAC?**
A hash is a deterministic fixed-length string of bits derived from data. An **HMAC** is a hash computed over the data **plus a secret key**, so it also authenticates the sender.

**30. What is TLS and how does public-key cryptography work here?**
TLS (Transport Layer Security) is the successor of SSL; it encrypts at the **TCP layer** using public-key cryptography. Every party has a public key (shared) and a private key (secret); you encrypt with your private key plus the recipient's public key, and decrypt with your own private key.

**31. What is Punycode used for?**
Converting Unicode (UTF-8) strings into basic ASCII, because **host names only understand ASCII**. It underlies **Internationalized Domain Names (IDN/IDNA)**. `punycode.toASCII('mañana.com')` → `xn--maana-pta.com`.

### Data layer

**32. What must you add to the MySQL connection object before you can create a table?**
The **`database`** property — you must define the database name when you create the connection.

**33. How do you know how many rows an UPDATE or DELETE touched?**
`result.affectedRows` in the query callback.

**34. What replaces a table in MongoDB, and which methods insert one vs. many documents?**
A **collection**. `insertOne(obj, cb)` inserts one document; `insert(arrayOfObjs, cb)` inserts many and reports `res.insertedCount`.

**35. How do you sort MongoDB results ascending and descending?**
`find().sort({name: 1})` for ascending, `{name: -1}` for descending.

### Express

**36. What is Express.js in one sentence?**
A fast, assertive, essential and moderate web framework of Node.js — a layer built on top of Node.js that helps manage a server and routes.

**37. What are the four core features of Express?**
Designing single-page, multi-page and hybrid applications; setting up middlewares to respond to HTTP requests; defining a routing table for actions based on HTTP method and URL; dynamically rendering HTML pages by passing arguments to templates.

**38. Where do GET parameters arrive, and where do POST parameters arrive?**
GET → **`req.query`**. POST → **`req.body`**, and `req.body` is **undefined by default** until you add body-parsing middleware such as **body-parser**.

**39. Compare GET and POST as the notes do.**
GET sends a limited amount of data in the **header** and is **not secure** because the data is visible in the URL bar; POST sends a large amount of data in the **body** and is secure because the data is not visible in the URL, but is not used as popularly; GET is more efficient and used more.

**40. What is the difference between `req.url` and `req.originalurl`?**
`req.originalurl` retains the **original** request URL, which allows `req.url` to be rewritten freely for internal routing.

**41. What does `req.xhr` tell you?**
It is `true` when the request's `X-Requested-With` header is `XMLHttpRequest`, i.e. the request came from a client library such as jQuery.

**42. What happens if you call `res.send()` twice?**
Once you call `res.send()`, `res.redirect()` or `res.render()`, you **cannot do it again** — otherwise there will be an uncaught error.

**43. What is the difference between `res.send`, `res.json`, `res.jsonp` and `res.render`?**
`res.send` sends an HTTP response of any type (Buffer, object, HTML string); `res.json` returns the response in JSON format; `res.jsonp` returns JSON with JSONP support; `res.render` renders a view (template) and sends the rendered HTML string to the client.

**44. What is the difference between `res.location(path)` and `res.redirect(path)`?**
`res.location` only **sets the `Location` header**; `res.redirect` sets the header **and** performs the redirect with an HTTP status.

**45. What is a middleware function and what four things can it do?**
A function with access to `req` and `res` in the request-response cycle. It can execute any code; make changes to the request and response objects; end the request-response cycle; and call the next middleware function in the stack via `next()`.

**46. In what order do middleware functions run?**
Always **in the order in which they are added** to the stack.

**47. Name the five types of Express middleware.**
Application-level, router-level, error-handling, built-in, and third-party.

**48. Which middleware do you use for cookies, form bodies and file uploads?**
**cookie-parser** (parses the Cookie header into `req.cookies`), **body-parser** (JSON, raw, text and URL-encoded bodies), **multer** (multipart/form-data file uploads).

**49. What are cookies and how does the exchange work?**
Small pieces of information sent from a website and stored in the user's browser. The browser sends them back to the server on every subsequent request to that website so the server can recognize the user: request → response + cookie → request + cookie.

**50. What does the route `'/ab*cd'` match?**
`abcd`, `abxcd`, `ab123cd` and so on — it is a pattern-matching route.

**51. What is scaffolding?**
A technique supported by some MVC frameworks that lets the programmer specify how application data may be used; the framework then uses predefined code templates to generate the final code for **CRUD** operations. Install with `npm install express-scaffold` and `npm install -g express-generator`.

**52. What two settings must you configure to use a template engine, and where do Pug files live?**
`app.set('views', './views')` and `app.set('view engine', 'pug')`. All `.pug` files must live in the **`views` folder in the root** of the application (by default), and Pug uses **whitespace and indentation** as part of its syntax.

---

# APPENDIX — Quick reference

### Node.js modules covered

`http` · `console` · `os` · timers (global) · `dns` · `net` · `crypto` · `tls` · `process` (global) · `child_process` · `Buffer` (global) · streams · `fs` · `path` · `string_decoder` · `querystring` · `zlib` · `assert` · `v8` · `events` · `punycode` · `tty` · `url` · `mysql` · `mongodb`

### Express API covered

`express()` · `app.get/post/delete` · `app.use` · `app.listen` · `app.set` · `express.static` · `req.query/body/params/cookies` · `res.send/json/jsonp/render/redirect/sendFile/download/status/type/set/cookie/clearCookie/end/format/append/attachment/links/location/get` · middleware + `next()` · body-parser · cookie-parser · multer · pug

### Suggested learning order for a beginner

1. Install Node, run `console_example1.js`, play in the REPL (A2, A4).
2. Learn npm and the command line options (A5, A6).
3. **Understand blocking vs non-blocking and callbacks** — this is the heart of Node (A27).
4. Events and EventEmitter (A28).
5. File system, paths, buffers and streams (A18–A21).
6. Build a raw HTTP server (A2, A31).
7. Move to Express: routing, req/res, GET/POST (B1–B7).
8. Middleware, cookies, file upload (B8–B10).
9. Databases — MySQL and MongoDB (A32, A33).
10. Templates with Pug (B12).
