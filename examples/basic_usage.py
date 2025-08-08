"""
PyMountain基础使用示例 | PyMountain basic usage example

演示PyMountain的基本功能和使用方法 | Demonstrates basic functionality and usage of PyMountain
"""

import numpy as np
import matplotlib.pyplot as plt
from pymountain import (
    MountainData,
    Matplotlib3DRenderer,
    MatplotlibContourRenderer,
    quick_render
)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def create_sample_mountain_data():
    """创建示例山体数据 | Create sample mountain data"""
    print("创建示例山体数据... | Creating sample mountain data...")

    # 创建山体数据对象 | Create mountain data object
    data = MountainData()

    # 添加一些示例数据点 | Add some sample data points
    # 创建一个简单的山峰形状 | Create a simple mountain peak shape
    np.random.seed(42)  # 确保结果可重现 | Ensure reproducible results

    # 生成网格点 | Generate grid points
    x_range = np.linspace(-10, 10, 20)
    y_range = np.linspace(-10, 10, 20)

    for x in x_range:
        for y in y_range:
            # 创建一个高斯山峰 | Create a Gaussian peak
            distance = np.sqrt(x ** 2 + y ** 2)
            elevation = 1000 * np.exp(-distance ** 2 / 50) + np.random.normal(0, 10)

            # 添加一些噪声和变化 | Add some noise and variation
            if distance < 5:
                elevation += 200 * np.exp(-distance ** 2 / 10)

            data.add_point(x, y, max(0, elevation))

    print(f"已添加 {len(data)} 个数据点 | Added {len(data)} data points")
    return data


def basic_3d_visualization():
    """基础3D可视化示例 | Basic 3D visualization example"""
    print("\n=== 基础3D可视化示例 | Basic 3D Visualization Example ===")

    # 创建数据 | Create data
    data = create_sample_mountain_data()

    # 创建3D渲染器 | Create 3D renderer
    renderer = Matplotlib3DRenderer(
        config={
            'title': '山体地形3D可视化 | Mountain Terrain 3D Visualization',
            'colormap': 'terrain',
            'figure_size': (12, 8),
            'elevation_angle': 30,
            'azimuth_angle': 45
        }
    )

    # 渲染数据 | Render data
    fig = renderer.render(data)

    # 保存图像 | Save image
    renderer.save_figure('output/basic_3d_mountain.png')
    print("3D可视化已保存到 output/basic_3d_mountain.png")

    # 显示图形 | Show figure
    renderer.show()

    return renderer


def basic_contour_visualization():
    """基础等高线可视化示例 | Basic contour visualization example"""
    print("\n=== 基础等高线可视化示例 | Basic Contour Visualization Example ===")

    # 创建数据 | Create data
    data = create_sample_mountain_data()

    # 创建等高线渲染器 | Create contour renderer
    renderer = MatplotlibContourRenderer(
        config={
            'title': '山体地形等高线图 | Mountain Terrain Contour Map',
            'colormap': 'terrain',
            'figure_size': (10, 8),
            'contour_levels': 15,
            'filled_contours': True,
            'show_contour_lines': True,
            'show_data_points': True
        }
    )

    # 渲染数据 | Render data
    fig = renderer.render(data)

    # 保存图像 | Save image
    renderer.save_figure('output/basic_contour_mountain.png')
    print("等高线可视化已保存到 output/basic_contour_mountain.png")

    # 显示图形 | Show figure
    renderer.show()

    return renderer


def quick_render_example():
    """快速渲染示例 | Quick render example"""
    print("\n=== 快速渲染示例 | Quick Render Example ===")

    # 创建简单的点数据 | Create simple point data
    points = [
        (0, 0, 100),
        (1, 0, 150),
        (0, 1, 120),
        (1, 1, 180),
        (0.5, 0.5, 200),
        (-1, 0, 80),
        (0, -1, 90),
        (-1, -1, 60)
    ]

    print(f"使用 {len(points)} 个点进行快速渲染 | Quick rendering with {len(points)} points")

    # 使用快速渲染功能 | Use quick render functionality
    renderer = quick_render(
        points,
        renderer_type="3d",
        title="快速渲染示例 | Quick Render Example",
        colormap="viridis"
    )

    # 保存图像 | Save image
    renderer.save_figure('output/quick_render_example.png')
    print("快速渲染结果已保存到 output/quick_render_example.png")

    # 显示图形 | Show figure
    renderer.show()

    return renderer


def data_manipulation_example():
    """数据操作示例 | Data manipulation example"""
    print("\n=== 数据操作示例 | Data Manipulation Example ===")

    # 创建空的数据对象 | Create empty data object
    data = MountainData()

    # 逐步添加数据点 | Add data points step by step
    print("添加数据点... | Adding data points...")
    for i in range(10):
        x = np.random.uniform(-5, 5)
        y = np.random.uniform(-5, 5)
        z = np.random.uniform(50, 200)
        data.add_point(x, y, z, metadata={'point_id': i, 'type': 'random'})

    print(f"当前数据点数量: {len(data)} | Current number of data points: {len(data)}")

    # 获取数据边界 | Get data bounds
    bounds = data.get_bounds()
    print(f"数据边界 | Data bounds: {bounds}")

    # 获取高程统计 | Get elevation statistics
    stats = data.get_elevation_stats()
    print(f"高程统计 | Elevation statistics: {stats}")

    # 更新某个点 | Update a point
    print("更新第一个点... | Updating first point...")
    data.update_point(0, z=300, metadata={'updated': True})

    # 获取区域内的点 | Get points in region
    region_points = data.get_points_in_region(-2, 2, -2, 2)
    print(f"区域内点数量: {len(region_points)} | Points in region: {len(region_points)}")

    # 转换为NumPy数组 | Convert to NumPy arrays
    x_array, y_array, z_array = data.to_numpy_arrays()
    print(f"NumPy数组形状 | NumPy array shapes: X{x_array.shape}, Y{y_array.shape}, Z{z_array.shape}")

    # 保存为JSON | Save as JSON
    json_str = data.to_json()
    print(f"JSON数据长度: {len(json_str)} 字符 | JSON data length: {len(json_str)} characters")

    # 保存到文件 | Save to file
    data.to_json('output/sample_data.json')
    print("数据已保存到 output/sample_data.json")

    return data


def load_and_visualize_example():
    """加载和可视化示例 | Load and visualize example"""
    print("\n=== 加载和可视化示例 | Load and Visualize Example ===")

    # 创建新的数据对象并从JSON加载 | Create new data object and load from JSON
    data = MountainData()

    try:
        data.load_from_json('output/sample_data.json')
        print(f"从JSON加载了 {len(data)} 个数据点 | Loaded {len(data)} data points from JSON")

        # 可视化加载的数据 | Visualize loaded data
        renderer = Matplotlib3DRenderer(
            config={
                'title': '从JSON加载的数据 | Data Loaded from JSON',
                'colormap': 'plasma',
                'marker_size': 50
            }
        )

        fig = renderer.render(data)
        renderer.save_figure('output/loaded_data_visualization.png')
        print("加载数据的可视化已保存到 output/loaded_data_visualization.png")

        renderer.show()

    except FileNotFoundError:
        print(
            "JSON文件未找到，请先运行 data_manipulation_example() | JSON file not found, please run data_manipulation_example() first")

    return data


def create_output_directory():
    """创建输出目录 | Create output directory"""
    import os
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建输出目录: {output_dir} | Created output directory: {output_dir}")


def main():
    """主函数 | Main function"""
    print("PyMountain基础使用示例 | PyMountain Basic Usage Examples")
    print("=" * 60)

    # 创建输出目录 | Create output directory
    create_output_directory()

    try:
        # 运行各种示例 | Run various examples
        basic_3d_visualization()
        basic_contour_visualization()
        quick_render_example()
        data_manipulation_example()
        load_and_visualize_example()

        print("\n=== 所有示例运行完成! | All Examples Completed! ===")
        print("请查看 output/ 目录中的输出文件 | Please check output files in output/ directory")

    except Exception as e:
        print(f"运行示例时出错 | Error running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
