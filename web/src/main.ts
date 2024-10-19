import {createApp} from 'vue'  // 创建应用实例
import './assets/css/reset.scss'  // 引入清除默认样式
import App from './App.vue'  // 引入根组件App
import Top from './components/top/Index.vue'
import Bottom from './components/bottom/Index.vue'

const app = createApp(App)
app.component('Top', Top);
app.component('Bottom', Bottom);
app.mount('#app')
