# PyMountain 示例代码 | PyMountain Examples

本目录包含了PyMountain库的各种使用示例，从基础入门到高级应用。
This directory contains various usage examples of the PyMountain library, from basic introduction to advanced applications.

## 示例文件说明 | Example Files Description

### 1. `quick_start.py` - 快速开始 | Quick Start
**适合人群 | Suitable for**: 初学者 | Beginners  
**运行时间 | Runtime**: ~2分钟 | ~2 minutes

最简单的PyMountain使用示例，包含：
Simplest PyMountain usage examples, including:

- 一行代码快速渲染 | One-line quick rendering
- 分步骤创建过程 | Step-by-step creation process
- 3D和等高线可视化 | 3D and contour visualization
- 随机数据生成 | Random data generation
- 图像保存功能 | Image saving functionality

```bash
python examples/quick_start.py
```

### 2. `basic_usage.py` - 基础使用 | Basic Usage
**适合人群 | Suitable for**: 有一定编程基础的用户 | Users with some programming background  
**运行时间 | Runtime**: ~5分钟 | ~5 minutes

展示PyMountain的核心功能，包含：
Demonstrates core PyMountain functionality, including:

- 创建复杂山体数据 | Creating complex mountain data
- 3D表面渲染 | 3D surface rendering
- 等高线图绘制 | Contour map plotting
- 数据操作和管理 | Data manipulation and management
- JSON数据导入导出 | JSON data import/export
- 数据统计分析 | Data statistical analysis

```bash
python examples/basic_usage.py
```

### 3. `advanced_usage.py` - 高级使用 | Advanced Usage
**适合人群 | Suitable for**: 高级用户和研究人员 | Advanced users and researchers  
**运行时间 | Runtime**: ~10分钟 | ~10 minutes

展示PyMountain的高级功能，包含：
Demonstrates advanced PyMountain functionality, including:

- 多种插值方法比较 | Multiple interpolation methods comparison
- 自定义颜色映射 | Custom color mapping
- 多渲染器对比 | Multi-renderer comparison
- 性能分析和优化 | Performance analysis and optimization
- 多格式数据导入导出 | Multi-format data import/export
- 大数据量处理 | Large dataset processing

```bash
python examples/advanced_usage.py
```

## 输出文件 | Output Files

运行示例后，生成的文件将保存在 `examples/output/` 目录中：
After running examples, generated files will be saved in the `examples/output/` directory:

```
examples/output/
├── basic_3d_mountain.png              # 基础3D山体图
├── basic_contour_mountain.png          # 基础等高线图
├── quick_render_example.png            # 快速渲染示例
├── loaded_data_visualization.png       # 加载数据可视化
├── my_first_mountain.png              # 第一座山
├── interpolation_comparison.png        # 插值方法比较
├── custom_color_mapping.png           # 自定义颜色映射
├── multi_renderer_comparison.png      # 多渲染器比较
├── performance_analysis.png           # 性能分析
├── sample_data.json                   # 示例数据JSON
├── mountain_data.json                 # 山体数据JSON
├── mountain_data.npz                  # NumPy格式数据
└── mountain_data.csv                  # CSV格式数据
```

## 运行要求 | Requirements

### 基础要求 | Basic Requirements
- Python 3.7+
- NumPy
- Matplotlib
- SciPy

### 可选依赖 | Optional Dependencies
- Pandas (用于CSV数据处理 | for CSV data processing)
- Plotly (用于交互式可视化 | for interactive visualization)
- PyQt/PySide (用于GUI应用 | for GUI applications)

## 安装和运行 | Installation and Running

1. **安装PyMountain | Install PyMountain**
   ```bash
   pip install -e .
   ```

2. **运行示例 | Run Examples**
   ```bash
   # 快速开始
   python examples/quick_start.py
   
   # 基础使用
   python examples/basic_usage.py
   
   # 高级使用
   python examples/advanced_usage.py
   ```

3. **查看输出 | View Output**
   ```bash
   # 查看生成的图像文件
   ls examples/output/
   ```

## 示例特色 | Example Features

### 🚀 快速上手 | Quick Start
- 零配置运行 | Zero-configuration running
- 详细的中英文注释 | Detailed bilingual comments
- 渐进式学习路径 | Progressive learning path

### 📊 丰富的可视化 | Rich Visualization
- 3D表面图 | 3D surface plots
- 等高线图 | Contour maps
- 自定义颜色映射 | Custom color mapping
- 多种渲染风格 | Multiple rendering styles

### 🔧 实用功能 | Practical Features
- 数据导入导出 | Data import/export
- 性能优化技巧 | Performance optimization tips
- 错误处理示例 | Error handling examples
- 最佳实践指导 | Best practices guidance

### 📈 性能分析 | Performance Analysis
- 不同数据量的性能测试 | Performance testing with different data sizes
- 内存使用优化 | Memory usage optimization
- 渲染效率分析 | Rendering efficiency analysis

## 常见问题 | FAQ

### Q: 示例运行失败怎么办？| What if examples fail to run?
A: 请检查依赖是否正确安装，特别是matplotlib和numpy。
Please check if dependencies are properly installed, especially matplotlib and numpy.

### Q: 如何自定义示例？| How to customize examples?
A: 可以修改示例代码中的参数，如颜色映射、数据点数量等。
You can modify parameters in the example code, such as color mapping, number of data points, etc.

### Q: 生成的图像质量如何调整？| How to adjust generated image quality?
A: 在保存图像时可以调整DPI参数：`renderer.save_figure('filename.png', dpi=300)`
You can adjust the DPI parameter when saving images: `renderer.save_figure('filename.png', dpi=300)`

### Q: 如何处理大数据集？| How to handle large datasets?
A: 参考 `advanced_usage.py` 中的性能分析示例，使用数据采样和分批处理。
Refer to the performance analysis example in `advanced_usage.py`, use data sampling and batch processing.

## 贡献示例 | Contributing Examples

欢迎贡献新的示例代码！请确保：
Welcome to contribute new example code! Please ensure:

1. 代码有详细的中英文注释 | Code has detailed bilingual comments
2. 包含错误处理 | Includes error handling
3. 遵循现有的代码风格 | Follows existing code style
4. 提供清晰的文档说明 | Provides clear documentation

## 许可证 | License

这些示例代码遵循与PyMountain主项目相同的许可证。
These example codes follow the same license as the main PyMountain project.

---

**开始你的PyMountain之旅！| Start your PyMountain journey!** 🏔️