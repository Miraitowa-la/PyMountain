# PyMountain 🏔️

**一个强大而灵活的Python山体地形数据可视化库**

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](#)

## 🌟 特性

### 🎯 核心功能
- **多种可视化方式**
  - 3D表面渲染
  - 等高线图
  - 散点图
  - 自定义渲染器

- **灵活的数据处理**
  - 支持多种数据格式
  - 数据插值和平滑
  - 统计分析功能
  - 数据导入导出

- **高度可定制**
  - 自定义颜色映射
  - 可配置渲染参数
  - 插件式架构
  - 主题和样式系统

### 🚀 性能优势
- **高效渲染**
- **内存优化**
- **大数据支持**
- **并行处理**

## 📦 安装

### 使用pip安装
```bash
pip install pymountain
```

### 从源码安装
```bash
git clone https://github.com/yourusername/pymountain.git
cd pymountain
pip install -e .
```

### 开发环境安装
```bash
git clone https://github.com/yourusername/pymountain.git
cd pymountain
pip install -e ".[dev]"
```

## 🚀 快速开始

### 30秒创建你的第一座山

```python
from pymountain import quick_render

# 定义山峰数据点 (x, y, elevation)
points = [
    (0, 0, 1000),    # 山峰
    (1, 0, 800),     # 东侧
    (-1, 0, 800),    # 西侧
    (0, 1, 750),     # 北侧
    (0, -1, 750),    # 南侧
]

# 一行代码完成3D可视化！
renderer = quick_render(points, renderer_type="3d", title="我的第一座山")
renderer.show()
```

### 更详细的使用方式

```python
from pymountain import MountainData, Matplotlib3DRenderer

# 创建数据对象
data = MountainData()

# 添加数据点
data.add_point(0, 0, 1000, metadata={'name': '主峰'})
data.add_point(1, 1, 800, metadata={'name': '次峰'})
data.add_point(-1, -1, 600, metadata={'name': '小峰'})

# 创建渲染器
renderer = Matplotlib3DRenderer(
    config={
        'title': '山体地形图',
        'colormap': 'terrain',
        'figure_size': (12, 8)
    }
)

# 渲染和显示
fig = renderer.render(data)
renderer.show()

# 保存图像
renderer.save_figure('my_mountain.png')
```

## 📚 文档和示例

### 📖 示例代码

我们提供了丰富的示例代码，帮助你快速上手：

```bash
# 快速开始示例
python examples/quick_start.py

# 基础使用示例
python examples/basic_usage.py

# 高级功能示例
python examples/advanced_usage.py
```

### 🎓 学习路径

1. **初学者**: 从 `examples/quick_start.py` 开始
2. **进阶用户**: 学习 `examples/basic_usage.py`
3. **高级用户**: 探索 `examples/advanced_usage.py`

## 🛠️ API 参考

### 核心类

#### `MountainData`
山体数据管理类

```python
from pymountain import MountainData

data = MountainData()
data.add_point(x, y, elevation, metadata={})
data.get_bounds()  # 获取数据边界
data.get_elevation_stats()  # 获取高程统计
```

#### `BaseRenderer`
渲染器基类

```python
from pymountain import Matplotlib3DRenderer

renderer = Matplotlib3DRenderer(config={
    'title': '标题',
    'colormap': 'terrain',
    'figure_size': (10, 8)
})
```

### 渲染器类型

| 渲染器 | 描述 | 适用场景 |
|--------|------|----------|
| `Matplotlib3DRenderer` | 3D表面渲染 | 立体地形展示 |
| `MatplotlibContourRenderer` | 等高线渲染 | 地形分析 |
| `MatplotlibRenderer` | 通用渲染器 | 自定义可视化 |

### 工具函数

#### 插值函数
```python
from pymountain.utils import (
    linear_interpolation,
    cubic_interpolation,
    rbf_interpolation
)

# 线性插值
zi = linear_interpolation(x, y, z, xi, yi)
```

#### 颜色映射
```python
from pymountain.utils import ColorMapper, create_elevation_colormap

# 创建自定义颜色映射
colormap = create_elevation_colormap({
    (0, 500): '#2E8B57',      # 低地
    (500, 1000): '#DAA520',   # 中山
    (1000, 2000): '#A0522D'   # 高山
})
```

## 🎨 高级功能

### 自定义颜色映射

```python
from pymountain import ColorMapper

# 创建颜色映射器
mapper = ColorMapper()

# 定义高程带颜色
elevation_colors = {
    (0, 200): '#2E8B57',      # 海绿色 - 低地
    (200, 600): '#DAA520',    # 金黄色 - 丘陵
    (600, 1000): '#A0522D',   # 赭石色 - 山地
    (1000, float('inf')): '#FFFFFF'  # 白色 - 雪峰
}

colormap = mapper.create_elevation_colormap(elevation_colors)
```

### 数据插值

```python
from pymountain.utils import interpolate_mountain_data

# 对稀疏数据进行插值
interpolated_data = interpolate_mountain_data(
    data, 
    method='cubic',
    grid_size=(100, 100)
)
```

### 性能优化

```python
# 大数据集处理建议
data = MountainData()

# 使用批量添加
points = [(x, y, z) for x, y, z in large_dataset]
data.add_points_batch(points)

# 使用数据采样
sampled_data = data.sample(max_points=1000)
```

## 📊 支持的数据格式

### 输入格式
- **NumPy数组**: `(x, y, z)` 坐标
- **Pandas DataFrame**: 包含坐标列的数据框
- **JSON文件**: 结构化的地形数据
- **CSV文件**: 逗号分隔的坐标数据
- **Python列表**: `[(x1, y1, z1), (x2, y2, z2), ...]`

### 输出格式
- **图像文件**: PNG, JPG, SVG, PDF
- **数据文件**: JSON, CSV, NumPy (.npz)
- **交互式图表**: HTML (通过Plotly)

## 🔧 配置选项

### 渲染器配置

```python
config = {
    # 基础设置
    'title': '山体地形图',
    'figure_size': (12, 8),
    'dpi': 300,
    
    # 颜色设置
    'colormap': 'terrain',
    'color_levels': 20,
    
    # 3D设置
    'elevation_angle': 30,
    'azimuth_angle': 45,
    'surface_alpha': 0.8,
    
    # 等高线设置
    'contour_levels': 15,
    'filled_contours': True,
    'show_contour_lines': True,
    
    # 数据点设置
    'show_data_points': True,
    'point_size': 50,
    'point_color': 'red'
}
```

## 🧪 测试

运行测试套件：

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_core.py

# 生成覆盖率报告
pytest --cov=pymountain
```

## 🤝 贡献

我们欢迎所有形式的贡献！

### 如何贡献

1. **Fork** 这个仓库
2. **创建** 特性分支
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **提交** 你的更改
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **推送** 到分支
   ```bash
   git push origin feature/amazing-feature
   ```
5. **打开** Pull Request

### 开发指南

- 遵循PEP 8代码风格
- 添加适当的测试
- 更新文档
- 确保所有测试通过

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢所有贡献者
- 基于优秀的开源库构建：
  - [NumPy](https://numpy.org/) - 数值计算
  - [Matplotlib](https://matplotlib.org/) - 数据可视化
  - [SciPy](https://scipy.org/) - 科学计算

## 📞 支持

- **文档**: [在线文档](https://pymountain.readthedocs.io/)
- **问题反馈**: [GitHub Issues](https://github.com/yourusername/pymountain/issues)
- **讨论**: [GitHub Discussions](https://github.com/yourusername/pymountain/discussions)
- **邮件**: support@pymountain.org

## 🗺️ 路线图

### v1.1 (计划中)
- [ ] 交互式3D可视化
- [ ] 更多渲染器支持
- [ ] 性能优化
- [ ] 移动端支持

### v1.2 (未来)
- [ ] 实时数据流处理
- [ ] 机器学习集成
- [ ] 云端渲染服务
- [ ] VR/AR支持

---

**开始你的山体可视化之旅！🏔️**

[⬆ 回到顶部](#pymountain-🏔️)