# python-wasm-component

Build a wasm component from a python http app

1. Create a wit directory with a world that conforms to an http trigger which essentially means you need a world that exports
a wasi http incoming handler type

2. Generate bindings using [componentize-py](https://github.com/bytecodealliance/componentize-py). By default, bindings will be created in a directory with the same name as the world you are targeting (replacing hyphens with underscores).

```bash
componentize-py -d wit -w http-app bindings .
```

3. Create the http handler in app.py using imports from the bindings that were generated.

4. Run `spin up --build` to build and run your component. Under the hood `spin build` is running `componentize-py -d wit -w http-app componentize app -o app.wasm` which builds you WASM component and outputs it as `app.wasm`.


Enjoy!