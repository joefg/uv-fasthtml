# uv-fasthtml project template

This is a very basic [FastHTML](https://fastht.ml) project template
which uses the [uv](https://github.com/astral-sh/uv) package manager.
It aims to introduce sound architecture and testing practices from day
one of a project.

## How to use it

A Runfile is provided for your convience. See all commands with `./run`.

`./run restore` fetches all dependencies, and `./run serve` spawns a
server.

When deploying to production, disable autoreload and hide it behind
a [reverse
proxy](https://www.digitalocean.com/community/tutorials/how-to-configure-nginx-as-a-reverse-proxy-on-ubuntu-22-04).

To get a GitHub OAuth token and secret, follow [this
guide](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app).

## TODO

- [x] Database
- [x] External JavaScript
- [x] Testing
- [x] OAuth Authentication
- [ ] Streaming content

## Why?

I don't think the coding style advocated in the [FastHTML
docs](https://fastht.ml/docs/) is particularly elegant, or makes for
production-ready code (which I consider to include unit and integration
testing along with CI). I would rather keep model logic separate from
page creation separate from the controllers so I can unit test the models
and integration test the page creation.

I'm also not sold on `fastlite`, in that I'm not sure how well it can
handle complex migrations. I appreciate that it hides some
complexity from the developer, it introduces some more when maintaining
the application. This is why I'm sticking with an old-fashioned set of
models to handle database transactions.

I like FastHTML. It does a lot of things well,
but the documentation contains butt-ugly code that could be made a lot
clearer. The nice thing about FastHTML is that it's not opinionated
out of the box, which means I can introduce my own into my work..
