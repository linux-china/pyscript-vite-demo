import {defineConfig} from "vite";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        pyscriptHmr()
    ]
});


function pyscriptHmr() {
    return {
        name: 'pyscript-hmr',
        enforce: 'post',
        handleHotUpdate({file, server}) {
            if (file.endsWith('.py')) {
                console.log('reloading Python file:', file);

                server.ws.send({
                    type: 'full-reload',
                    path: '*.py'
                });
            }
        },
    }
}