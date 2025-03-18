<template>
  <div class="center">
    <h1>登录/注册</h1>
    <div class="logon">
      <div :class="overlaylong">
        <div class="overlaylong-Signin">
          <h2 class="overlaylongH2">Sign in</h2>
          <form @submit.prevent="handleLogin">
            <input type="text" placeholder="username" v-model="username" required />
            <input type="password" placeholder="password" v-model="password" required />
            <h3>Forgot your password?</h3>
            <button class="inupbutton" type="submit">登录</button>
          </form>
        </div>
      </div>
      <div :class="overlaytitle">
        <div class="overlaytitle-Signin">
          <h2 class="overlaytitleH2">Hello, Friend!</h2>
          <p class="overlaytitleP">Enter your personal details and start your journey with us</p>
          <div class="buttongohs" @click="Signin">Sign up</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import router from '../router'; // 引入路由实例

export default {
  data() {
    return {
      username: '',
      password: '',
      overlaylong: 'overlaylong',
      overlaytitle: 'overlaytitle',
      disfiex: 0 // 用于控制登录/注册切换，当前只实现登录
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('http://localhost:8000/login', {
          username: this.username,
          password: this.password
        });
        if (response.data.success) {
          alert('登录成功');
          localStorage.setItem('token', response.data.token); // 保存 token
          router.push('/');
        } else {
          alert('登录失败，请检查用户名和密码');
        }
      } catch (error) {
        console.error('登录错误:', error);
        alert('登录错误，请稍后再试');
      }
    },
    Signin() {
      // 可选：如果需要实现注册切换功能，可以在这里扩展
      // 当前仅保留登录界面，点击 Sign up 无实际跳转
      console.log('Sign up clicked - 暂未实现注册功能');
    }
  }
};
</script>

<style scoped>
.center {
  width: 100vw; /* 修改为视口宽度 */
  height: 100vh; /* 修改为视口高度 */
  background-image: url('../assets/imgs/heart-1381463_1920.jpg'); /* 设置背景图片 */
  background-size: cover; /* 修改为 cover 以适应视口 */
  background-repeat: no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

h1 {
  font-size: 30px;
  color: black;
  font-family: Arial, sans-serif; /* 添加字体样式 */
}

.logon {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  width: 768px;
  max-width: 100%;
  min-height: 480px;
  margin-top: 20px;
  display: flex;
  background: -webkit-linear-gradient(right, #4284db, #29eac4);
}

.overlaylong {
  border-radius: 10px 0 0 10px;
  width: 50%;
  height: 100%;
  background-color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column; /* 添加 flex 布局 */
  text-align: center; /* 添加文本居中对齐 */
}

.overlaytitle {
  border-radius: 0px 10px 10px 0px;
  width: 50%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column; /* 添加 flex 布局 */
  text-align: center; /* 添加文本居中对齐 */
}

.overlaytitleH2 {
  font-size: 30px;
  color: #fff;
  margin-top: 20px;
  font-family: Arial, sans-serif; /* 添加字体样式 */
}

.overlaytitleP {
  font-size: 15px;
  color: #fff;
  margin-top: 20px;
  font-family: Arial, sans-serif; /* 添加字体样式 */
}

.overlaylong-Signin {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center; /* 添加文本居中对齐 */
}

.overlaylongH2 {
  font-size: 25px;
  color: black;
  font-family: Arial, sans-serif; /* 添加字体样式 */
}

input {
  background-color: #eee;
  border: none;
  padding: 12px 15px;
  margin: 10px 0;
  width: 240px;
  font-family: Arial, sans-serif; /* 添加字体样式 */
  text-align: center; /* 添加输入框文本居中对齐 */
}

h3 {
  font-size: 10px;
  margin-top: 10px;
  cursor: pointer;
  font-family: Arial, sans-serif; /* 添加字体样式 */
}

.inupbutton {
  background-color: #29eac4;
  border: none;
  width: 180px;
  height: 40px;
  border-radius: 50px;
  font-size: 15px;
  color: #fff;
  text-align: center;
  line-height: 40px;
  margin-top: 30px;
  cursor: pointer;
  font-family: Arial, sans-serif; /* 添加字体样式 */
}

.buttongohs {
  width: 180px;
  height: 40px;
  border-radius: 50px;
  border: 1px solid #fff;
  color: #fff;
  font-size: 15px;
  text-align: center;
  line-height: 40px;
  margin-top: 40px;
  margin-left: 95px;
  cursor: pointer;
  font-family: Arial, sans-serif; /* 添加字体样式 */
  display: flex; /* 添加 flex 布局 */
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
}
</style>