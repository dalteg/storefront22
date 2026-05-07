services:
  - type: web
    name: storefront22
    env: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn storefront22.wsgi:application"