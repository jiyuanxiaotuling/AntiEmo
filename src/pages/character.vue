<template>
    <div ref="threeContainer" style="width: 100%; height: 100vh;"></div>
</template>
  
  <script >
  import * as THREE from 'three';
  import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
  
  export default {
    name: 'ThreeScene',
    mounted() {
      this.initThree();
    },
    methods: {
      initThree() {
        const container = this.$refs.threeContainer;
        if (!container) {
          console.error('Container not found');
          return;
        }
  
        // 初始化场景、相机和渲染器
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        container.appendChild(renderer.domElement);
  
        // 添加光源
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // 环境光
        scene.add(ambientLight);
        const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // 方向光
        directionalLight.position.set(5, 5, 5);
        scene.add(directionalLight);
  
        // 加载模型
        const loader = new GLTFLoader();
        loader.load(
          '../public/scene.gltf', // 使用 public 目录下的路径
          (gltf) => {
            console.log('Model loaded successfully:', gltf);
            const model = gltf.scene;
            scene.add(model);
  
            // 调整相机位置以适应模型
            const box = new THREE.Box3().setFromObject(model);
            const center = box.getCenter(new THREE.Vector3());
            const size = box.getSize(new THREE.Vector3());
            const maxDim = Math.max(size.x, size.y, size.z);
            camera.position.set(center.x, center.y, maxDim * 2);
            camera.lookAt(center);
          },
          (progress) => {
            console.log('Loading progress:', progress.loaded / progress.total * 100 + '%');
          },
          (error) => {
            console.error('Error loading model:', error);
          }
        );
  
        // 添加坐标轴辅助（调试用）
        const axesHelper = new THREE.AxesHelper(5);
        scene.add(axesHelper);
  
        // 渲染循环
        const animate = () => {
          requestAnimationFrame(animate);
          renderer.render(scene, camera);
        };
        animate();
  
        // 窗口大小调整
        window.addEventListener('resize', () => {
          camera.aspect = window.innerWidth / window.innerHeight;
          camera.updateProjectionMatrix();
          renderer.setSize(window.innerWidth, window.innerHeight);
        });
      }
    }
  };
  </script>