"""
PyMountain快速开始示例 | PyMountain quick start example

最简单的PyMountain使用示例，适合初学者快速上手
Simplest PyMountain usage example, suitable for beginners to get started quickly
"""

import numpy as np
from pymountain import MountainData, quick_render


def simple_mountain():
    """创建一个简单的山峰 | Create a simple mountain peak"""
    print("创建简单山峰数据... | Creating simple mountain peak data...")
    
    # 定义一些简单的点 | Define some simple points
    points = [
        # (x, y, elevation)
        (0, 0, 1000),    # 山峰 | Peak
        (1, 0, 800),     # 东侧 | East side
        (-1, 0, 800),    # 西侧 | West side
        (0, 1, 750),     # 北侧 | North side
        (0, -1, 750),    # 南侧 | South side
        (1, 1, 600),     # 东北 | Northeast
        (-1, 1, 600),    # 西北 | Northwest
        (1, -1, 600),    # 东南 | Southeast
        (-1, -1, 600),   # 西南 | Southwest
        (2, 0, 400),     # 远东 | Far east
        (-2, 0, 400),    # 远西 | Far west
        (0, 2, 350),     # 远北 | Far north
        (0, -2, 350),    # 远南 | Far south
    ]
    
    print(f"使用 {len(points)} 个点创建山峰 | Creating mountain with {len(points)} points")
    return points


def method1_quick_render():
    """方法1：使用快速渲染功能 | Method 1: Using quick render function"""
    print("\n=== 方法1：快速渲染 | Method 1: Quick Render ===")
    
    # 创建数据 | Create data
    points = simple_mountain()
    
    # 一行代码完成渲染！| One line of code to complete rendering!
    renderer = quick_render(
        points, 
        renderer_type="3d",
        title="我的第一座山 | My First Mountain",
        colormap="terrain"
    )
    
    print("3D山峰渲染完成！| 3D mountain rendering completed!")
    
    # 显示图形 | Show figure
    renderer.show()
    
    return renderer


def method2_step_by_step():
    """方法2：分步骤创建 | Method 2: Step by step creation"""
    print("\n=== 方法2：分步骤创建 | Method 2: Step by Step Creation ===")
    
    # 第1步：创建数据对象 | Step 1: Create data object
    data = MountainData()
    print("步骤1：创建数据对象 | Step 1: Created data object")
    
    # 第2步：添加数据点 | Step 2: Add data points
    points = simple_mountain()
    for x, y, z in points:
        data.add_point(x, y, z)
    print(f"步骤2：添加了 {len(data)} 个数据点 | Step 2: Added {len(data)} data points")
    
    # 第3步：创建渲染器 | Step 3: Create renderer
    from pymountain import Matplotlib3DRenderer
    
    renderer = Matplotlib3DRenderer(
        config={
            'title': '分步创建的山峰 | Step-by-Step Created Mountain',
            'colormap': 'viridis',
            'figure_size': (10, 8)
        }
    )
    print("步骤3：创建渲染器 | Step 3: Created renderer")
    
    # 第4步：渲染数据 | Step 4: Render data
    fig = renderer.render(data)
    print("步骤4：渲染完成 | Step 4: Rendering completed")
    
    # 第5步：显示结果 | Step 5: Show result
    renderer.show()
    print("步骤5：显示图形 | Step 5: Displayed figure")
    
    return renderer, data


def method3_contour_map():
    """方法3：创建等高线图 | Method 3: Create contour map"""
    print("\n=== 方法3：等高线图 | Method 3: Contour Map ===")
    
    # 创建数据 | Create data
    data = MountainData()
    points = simple_mountain()
    
    for x, y, z in points:
        data.add_point(x, y, z)
    
    # 创建等高线渲染器 | Create contour renderer
    from pymountain import MatplotlibContourRenderer
    
    renderer = MatplotlibContourRenderer(
        config={
            'title': '山峰等高线图 | Mountain Contour Map',
            'colormap': 'terrain',
            'contour_levels': 10,
            'filled_contours': True,
            'show_data_points': True
        }
    )
    
    # 渲染 | Render
    fig = renderer.render(data)
    print("等高线图渲染完成！| Contour map rendering completed!")
    
    # 显示 | Show
    renderer.show()
    
    return renderer


def random_mountain_example():
    """随机山峰示例 | Random mountain example"""
    print("\n=== 随机山峰示例 | Random Mountain Example ===")
    
    # 生成随机山峰数据 | Generate random mountain data
    np.random.seed(42)  # 确保结果可重现 | Ensure reproducible results
    
    points = []
    for i in range(20):
        x = np.random.uniform(-3, 3)
        y = np.random.uniform(-3, 3)
        # 创建一个中心高、边缘低的分布 | Create a distribution high in center, low at edges
        distance_from_center = np.sqrt(x**2 + y**2)
        elevation = 800 * np.exp(-distance_from_center**2 / 5) + np.random.normal(0, 50)
        elevation = max(100, elevation)  # 确保最小高度 | Ensure minimum elevation
        
        points.append((x, y, elevation))
    
    print(f"生成了 {len(points)} 个随机点 | Generated {len(points)} random points")
    
    # 快速渲染 | Quick render
    renderer = quick_render(
        points,
        renderer_type="3d",
        title="随机生成的山峰 | Randomly Generated Mountain",
        colormap="plasma"
    )
    
    print("随机山峰渲染完成！| Random mountain rendering completed!")
    renderer.show()
    
    return renderer


def save_example():
    """保存示例 | Save example"""
    print("\n=== 保存示例 | Save Example ===")
    
    # 创建数据和渲染器 | Create data and renderer
    points = simple_mountain()
    renderer = quick_render(
        points,
        renderer_type="3d",
        title="保存的山峰图 | Saved Mountain Figure",
        colormap="coolwarm"
    )
    
    # 保存图像 | Save image
    import os
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = 'output/my_first_mountain.png'
    renderer.save_figure(filename)
    print(f"图像已保存到: {filename} | Image saved to: {filename}")
    
    # 也可以显示 | Can also show
    renderer.show()
    
    return renderer


def main():
    """主函数 - 运行所有快速开始示例 | Main function - run all quick start examples"""
    print("PyMountain快速开始指南 | PyMountain Quick Start Guide")
    print("=" * 60)
    print("这个示例将展示PyMountain的基本用法 | This example demonstrates basic PyMountain usage")
    print("每个方法都会创建并显示一个山峰可视化 | Each method creates and displays a mountain visualization")
    print()
    
    try:
        # 运行所有示例 | Run all examples
        method1_quick_render()
        method2_step_by_step()
        method3_contour_map()
        random_mountain_example()
        save_example()
        
        print("\n=== 快速开始示例完成! | Quick Start Examples Completed! ===")
        print("恭喜！你已经学会了PyMountain的基本用法 | Congratulations! You've learned basic PyMountain usage")
        print("接下来可以尝试 basic_usage.py 和 advanced_usage.py | Next, try basic_usage.py and advanced_usage.py")
        
    except Exception as e:
        print(f"运行示例时出错 | Error running examples: {e}")
        print("请确保已正确安装PyMountain及其依赖 | Please ensure PyMountain and its dependencies are properly installed")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()