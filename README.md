PyScript development with Vite.js
============================


# Requirements

* Python 3.10
* Node.js 16.15.0

# Features

* Language injection by PyCharm
* Auto reload by Vite.js

# PyCharm setup

* Install `Node.js` plugin on PyCharm
* Open PyCharm settings, choose `Edit -> Language Injections` and add injection for `py-env` and `py-script` as
  following:
    - py-env injection

  ![py-env injection](./docs/images/py-env-injection.png)
    - py-script injection: please add comment after `py-script` tag to prevent code format problem.

  ![py-script injection](./docs/images/py-script-injection.png)

# Development

* Install dependencies: `npm install`
* Run dev server: `npm run dev`

# why js.py?

js.py is a stub fake module for js module from PyScript, and it is used for code completion.

```python
from js import console

console.log('Hello, world!')
```

# Tips

* Please put `py-script` tag under body tag and before `</body>`

# References

* PyScript: https://github.com/pyscript/pyscript
* Vite.js: https://vitejs.dev/