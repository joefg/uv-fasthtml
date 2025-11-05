# uv-fasthtml project template

This is a very basic [FastHTML](https://fastht.ml) project template
which uses the [uv](https://github.com/astral-sh/uv) package manager.
It aims to introduce sound architecture and testing practices from day
one of a project.

## How to use it

A Runfile is provided for your convience. See all commands with `./run`.

`./run restore` fetches all dependencies, and `./run serve` spawns a
server. To stop the server, run `./run stop`.

When deploying to production, disable autoreload and hide it behind
a reverse proxy.

For this, I recommend using [Caddy](https://caddyserver.com/docs/quick-starts/reverse-proxy).
An example `Caddyfile` is provided for your convenience.

To get a GitHub OAuth token and secret, follow [this
guide](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app).

## TODO

- [x] Database
- [x] External JavaScript
- [x] Testing
- [x] OAuth Authentication
- [ ] Streaming content
