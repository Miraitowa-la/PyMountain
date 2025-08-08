"""
PyMountain高级使用示例 | PyMountain advanced usage example

演示PyMountain的高级功能，包括插值、颜色映射和自定义配置
Demonstrates advanced functionality of PyMountain including interpolation, color mapping and custom configurations
"""

import numpy as np
import matplotlib.pyplot as plt
from pymountain import (
    MountainData,
    Matplotlib3DRenderer,
    MatplotlibContourRenderer,
    ColorMapper,
    linear_interpolation,
    cubic_interpolation,
    rbf_interpolation,
    create_elevation_colormap,
    apply_color_mapping
)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def create_sparse_mountain_data():
    """创建稀疏的山体数据用于插值演示 | Create sparse mountain data for interpolation demonstration"""
    print("创建稀疏山体数据... | Creating sparse mountain data...")

    data = MountainData()

    # 创建一个更复杂的地形，包含多个峰和谷
    # Create a more complex terrain with multiple peaks and valleys
    peaks = [
        (0, 0, 1000),  # 主峰 | Main peak
        (-5, 3, 800),  # 次峰1 | Secondary peak 1
        (4, -2, 750),  # 次峰2 | Secondary peak 2
        (-3, -4, 600),  # 小峰 | Small peak
        (6, 5, 650),  # 边缘峰 | Edge peak
    ]

    valleys = [
        (2, 2, 200),  # 谷地1 | Valley 1
        (-2, 1, 150),  # 谷地2 | Valley 2
        (1, -3, 180),  # 谷地3 | Valley 3
        (-4, 2, 120),  # 谷地4 | Valley 4
    ]

    # 添加峰值点 | Add peak points
    for i, (x, y, z) in enumerate(peaks):
        data.add_point(x, y, z, metadata={'type': 'peak', 'id': i})

    # 添加谷值点 | Add valley points
    for i, (x, y, z) in enumerate(valleys):
        data.add_point(x, y, z, metadata={'type': 'valley', 'id': i})

    # 添加一些随机的中间点 | Add some random intermediate points
    np.random.seed(123)
    for _ in range(15):
        x = np.random.uniform(-7, 7)
        y = np.random.uniform(-6, 6)
        # 基于距离最近峰值的高度 | Height based on distance to nearest peak
        min_dist = float('inf')
        base_elevation = 0
        for px, py, pz in peaks:
            dist = np.sqrt((x - px) ** 2 + (y - py) ** 2)
            if dist < min_dist:
                min_dist = dist
                base_elevation = pz * np.exp(-dist ** 2 / 20) + np.random.normal(0, 50)

        data.add_point(x, y, max(50, base_elevation), metadata={'type': 'intermediate'})

    print(f"创建了 {len(data)} 个稀疏数据点 | Created {len(data)} sparse data points")
    return data


def interpolation_comparison():
    """插值方法比较示例 | Interpolation methods comparison example"""
    print("\n=== 插值方法比较 | Interpolation Methods Comparison ===")

    # 创建稀疏数据 | Create sparse data
    data = create_sparse_mountain_data()

    # 获取数据数组 | Get data arrays
    x_data, y_data, z_data = data.to_numpy_arrays()

    # 创建插值网格 | Create interpolation grid
    x_min, x_max = x_data.min() - 1, x_data.max() + 1
    y_min, y_max = y_data.min() - 1, y_data.max() + 1

    xi = np.linspace(x_min, x_max, 50)
    yi = np.linspace(y_min, y_max, 50)
    xi_grid, yi_grid = np.meshgrid(xi, yi)

    # 测试不同的插值方法 | Test different interpolation methods
    interpolation_methods = {
        'Linear': linear_interpolation,
        'Cubic': cubic_interpolation,
        'RBF': rbf_interpolation
    }

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('插值方法比较 | Interpolation Methods Comparison', fontsize=16)

    # 原始数据散点图 | Original data scatter plot
    ax = axes[0, 0]
    scatter = ax.scatter(x_data, y_data, c=z_data, cmap='terrain', s=100, edgecolors='black')
    ax.set_title('原始稀疏数据 | Original Sparse Data')
    ax.set_xlabel('X坐标 | X Coordinate')
    ax.set_ylabel('Y坐标 | Y Coordinate')
    plt.colorbar(scatter, ax=ax, label='高程 | Elevation')

    # 对每种插值方法进行可视化 | Visualize each interpolation method
    for idx, (method_name, interpolation_func) in enumerate(interpolation_methods.items()):
        print(f"执行 {method_name} 插值... | Performing {method_name} interpolation...")

        try:
            # 执行插值 | Perform interpolation
            zi = interpolation_func(x_data, y_data, z_data, xi_grid, yi_grid)

            # 绘制结果 | Plot results
            row = (idx + 1) // 2
            col = (idx + 1) % 2
            ax = axes[row, col]

            contour = ax.contourf(xi_grid, yi_grid, zi, levels=20, cmap='terrain')
            ax.scatter(x_data, y_data, c='red', s=30, edgecolors='black', alpha=0.8)
            ax.set_title(f'{method_name} 插值结果 | {method_name} Interpolation')
            ax.set_xlabel('X坐标 | X Coordinate')
            ax.set_ylabel('Y坐标 | Y Coordinate')
            plt.colorbar(contour, ax=ax, label='高程 | Elevation')

        except Exception as e:
            print(f"{method_name} 插值失败: {e} | {method_name} interpolation failed: {e}")
            ax = axes[row, col]
            ax.text(0.5, 0.5, f'{method_name}\n插值失败\nInterpolation Failed',
                    ha='center', va='center', transform=ax.transAxes, fontsize=12)
            ax.set_title(f'{method_name} 插值 | {method_name} Interpolation')

    plt.tight_layout()
    plt.savefig('output/interpolation_comparison.png', dpi=300, bbox_inches='tight')
    print("插值比较结果已保存到 output/interpolation_comparison.png")
    plt.show()

    return data


def custom_color_mapping_example():
    """自定义颜色映射示例 | Custom color mapping example"""
    print("\n=== 自定义颜色映射示例 | Custom Color Mapping Example ===")

    # 创建数据 | Create data
    data = create_sparse_mountain_data()

    # 创建自定义颜色映射器 | Create custom color mapper
    color_mapper = ColorMapper()

    # 定义高程带和对应颜色 | Define elevation bands and corresponding colors
    elevation_bands = {
        (0, 200): '#2E8B57',  # 海绿色 - 低地 | Sea green - lowlands
        (200, 400): '#9ACD32',  # 黄绿色 - 丘陵 | Yellow green - hills
        (400, 600): '#DAA520',  # 金黄色 - 中山 | Golden - medium mountains
        (600, 800): '#CD853F',  # 秘鲁色 - 高山 | Peru - high mountains
        (800, 1000): '#A0522D',  # 赭石色 - 山峰 | Sienna - peaks
        (1000, float('inf')): '#FFFFFF'  # 白色 - 雪峰 | White - snow peaks
    }

    # 创建高程颜色映射 | Create elevation color mapping
    custom_colormap = create_elevation_colormap(elevation_bands)

    # 使用自定义颜色映射进行渲染 | Render with custom color mapping
    renderer = Matplotlib3DRenderer(
        config={
            'title': '自定义颜色映射 | Custom Color Mapping',
            'colormap': custom_colormap,
            'figure_size': (12, 8),
            'elevation_angle': 25,
            'azimuth_angle': 60,
            'marker_size': 80
        }
    )

    fig = renderer.render(data)
    renderer.save_figure('output/custom_color_mapping.png')
    print("自定义颜色映射结果已保存到 output/custom_color_mapping.png")
    renderer.show()

    return renderer


def multi_renderer_comparison():
    """多渲染器比较示例 | Multi-renderer comparison example"""
    print("\n=== 多渲染器比较示例 | Multi-renderer Comparison Example ===")

    # 创建数据 | Create data
    data = create_sparse_mountain_data()

    # 创建子图 | Create subplots
    fig = plt.figure(figsize=(16, 8))

    # 3D渲染器配置 | 3D renderer configuration
    renderer_3d = Matplotlib3DRenderer(
        config={
            'title': '3D山体渲染 | 3D Mountain Rendering',
            'colormap': 'terrain',
            'elevation_angle': 30,
            'azimuth_angle': 45,
            'marker_size': 60,
            'surface_alpha': 0.8
        }
    )

    # 等高线渲染器配置 | Contour renderer configuration
    renderer_contour = MatplotlibContourRenderer(
        config={
            'title': '等高线地形图 | Contour Terrain Map',
            'colormap': 'terrain',
            'contour_levels': 20,
            'filled_contours': True,
            'show_contour_lines': True,
            'show_data_points': True,
            'point_size': 40
        }
    )

    # 渲染3D视图 | Render 3D view
    ax1 = fig.add_subplot(121, projection='3d')
    renderer_3d.ax = ax1
    renderer_3d.render(data)

    # 渲染等高线视图 | Render contour view
    ax2 = fig.add_subplot(122)
    renderer_contour.ax = ax2
    renderer_contour.render(data)

    plt.tight_layout()
    plt.savefig('output/multi_renderer_comparison.png', dpi=300, bbox_inches='tight')
    print("多渲染器比较结果已保存到 output/multi_renderer_comparison.png")
    plt.show()

    return fig


def performance_analysis():
    """性能分析示例 | Performance analysis example"""
    print("\n=== 性能分析示例 | Performance Analysis Example ===")

    import time

    # 测试不同数据量的性能 | Test performance with different data sizes
    data_sizes = [100, 500, 1000, 2000]
    performance_results = {}

    for size in data_sizes:
        print(f"测试数据量: {size} 点 | Testing data size: {size} points")

        # 创建测试数据 | Create test data
        data = MountainData()
        np.random.seed(42)

        start_time = time.time()

        # 生成随机山体数据 | Generate random mountain data
        for i in range(size):
            x = np.random.uniform(-10, 10)
            y = np.random.uniform(-10, 10)
            z = 500 * np.exp(-(x ** 2 + y ** 2) / 50) + np.random.normal(0, 20)
            data.add_point(x, y, max(0, z))

        data_creation_time = time.time() - start_time

        # 测试渲染性能 | Test rendering performance
        start_time = time.time()

        renderer = Matplotlib3DRenderer(
            config={
                'title': f'性能测试 - {size} 点 | Performance Test - {size} points',
                'colormap': 'viridis'
            }
        )

        fig = renderer.render(data)
        rendering_time = time.time() - start_time

        # 保存结果 | Save results
        performance_results[size] = {
            'data_creation_time': data_creation_time,
            'rendering_time': rendering_time,
            'total_time': data_creation_time + rendering_time
        }

        print(f"  数据创建时间: {data_creation_time:.3f}s | Data creation time: {data_creation_time:.3f}s")
        print(f"  渲染时间: {rendering_time:.3f}s | Rendering time: {rendering_time:.3f}s")
        print(
            f"  总时间: {data_creation_time + rendering_time:.3f}s | Total time: {data_creation_time + rendering_time:.3f}s")

        plt.close(fig)  # 关闭图形以节省内存 | Close figure to save memory

    # 绘制性能图表 | Plot performance chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    sizes = list(performance_results.keys())
    creation_times = [performance_results[s]['data_creation_time'] for s in sizes]
    rendering_times = [performance_results[s]['rendering_time'] for s in sizes]
    total_times = [performance_results[s]['total_time'] for s in sizes]

    # 时间对比图 | Time comparison chart
    ax1.plot(sizes, creation_times, 'o-', label='数据创建 | Data Creation', linewidth=2)
    ax1.plot(sizes, rendering_times, 's-', label='渲染 | Rendering', linewidth=2)
    ax1.plot(sizes, total_times, '^-', label='总计 | Total', linewidth=2)
    ax1.set_xlabel('数据点数量 | Number of Data Points')
    ax1.set_ylabel('时间 (秒) | Time (seconds)')
    ax1.set_title('性能分析 | Performance Analysis')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 渲染效率图 | Rendering efficiency chart
    efficiency = [s / t for s, t in zip(sizes, rendering_times)]
    ax2.plot(sizes, efficiency, 'o-', color='green', linewidth=2)
    ax2.set_xlabel('数据点数量 | Number of Data Points')
    ax2.set_ylabel('渲染效率 (点/秒) | Rendering Efficiency (points/sec)')
    ax2.set_title('渲染效率 | Rendering Efficiency')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('output/performance_analysis.png', dpi=300, bbox_inches='tight')
    print("性能分析结果已保存到 output/performance_analysis.png")
    plt.show()

    return performance_results


def data_export_import_example():
    """数据导出导入示例 | Data export/import example"""
    print("\n=== 数据导出导入示例 | Data Export/Import Example ===")

    # 创建原始数据 | Create original data
    original_data = create_sparse_mountain_data()
    print(f"原始数据点数量: {len(original_data)} | Original data points: {len(original_data)}")

    # 导出为不同格式 | Export to different formats
    formats_to_test = ['json', 'numpy', 'pandas']

    for fmt in formats_to_test:
        print(f"\n测试 {fmt.upper()} 格式 | Testing {fmt.upper()} format")

        try:
            if fmt == 'json':
                # JSON导出导入 | JSON export/import
                json_file = 'output/mountain_data.json'
                original_data.to_json(json_file)
                print(f"数据已导出到 {json_file} | Data exported to {json_file}")

                # 导入并验证 | Import and verify
                imported_data = MountainData()
                imported_data.load_from_json(json_file)
                print(f"从JSON导入了 {len(imported_data)} 个点 | Imported {len(imported_data)} points from JSON")

            elif fmt == 'numpy':
                # NumPy数组导出导入 | NumPy array export/import
                x_arr, y_arr, z_arr = original_data.to_numpy_arrays()
                np.savez('output/mountain_data.npz', x=x_arr, y=y_arr, z=z_arr)
                print("数据已导出到 mountain_data.npz | Data exported to mountain_data.npz")

                # 导入并验证 | Import and verify
                loaded_arrays = np.load('output/mountain_data.npz')
                imported_data = MountainData()
                imported_data.from_numpy_arrays(loaded_arrays['x'], loaded_arrays['y'], loaded_arrays['z'])
                print(f"从NumPy导入了 {len(imported_data)} 个点 | Imported {len(imported_data)} points from NumPy")

            elif fmt == 'pandas':
                # Pandas DataFrame导出导入 | Pandas DataFrame export/import
                try:
                    import pandas as pd
                    df = original_data.to_pandas_dataframe()
                    df.to_csv('output/mountain_data.csv', index=False)
                    print("数据已导出到 mountain_data.csv | Data exported to mountain_data.csv")

                    # 导入并验证 | Import and verify
                    loaded_df = pd.read_csv('output/mountain_data.csv')
                    imported_data = MountainData()
                    imported_data.from_pandas_dataframe(loaded_df)
                    print(
                        f"从Pandas导入了 {len(imported_data)} 个点 | Imported {len(imported_data)} points from Pandas")

                except ImportError:
                    print("Pandas未安装，跳过此格式 | Pandas not installed, skipping this format")
                    continue

            # 验证数据完整性 | Verify data integrity
            if len(imported_data) == len(original_data):
                print(f"✓ {fmt.upper()} 格式数据完整性验证通过 | {fmt.upper()} format data integrity verified")
            else:
                print(
                    f"✗ {fmt.upper()} 格式数据完整性验证失败 | {fmt.upper()} format data integrity verification failed")

        except Exception as e:
            print(f"✗ {fmt.upper()} 格式测试失败: {e} | {fmt.upper()} format test failed: {e}")

    return original_data


def create_output_directory():
    """创建输出目录 | Create output directory"""
    import os
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建输出目录: {output_dir} | Created output directory: {output_dir}")


def main():
    """主函数 | Main function"""
    print("PyMountain高级使用示例 | PyMountain Advanced Usage Examples")
    print("=" * 70)

    # 创建输出目录 | Create output directory
    create_output_directory()

    try:
        # 运行高级示例 | Run advanced examples
        interpolation_comparison()
        custom_color_mapping_example()
        multi_renderer_comparison()
        performance_analysis()
        data_export_import_example()

        print("\n=== 所有高级示例运行完成! | All Advanced Examples Completed! ===")
        print("请查看 output/ 目录中的输出文件 | Please check output files in output/ directory")

    except Exception as e:
        print(f"运行高级示例时出错 | Error running advanced examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
