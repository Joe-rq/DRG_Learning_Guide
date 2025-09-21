#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DRG分组可视化使用示例
演示如何使用本项目进行DRG分组学习和分析
"""

import sys
import os

# 添加src目录到路径，以便导入模块
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

def example_1_generate_all_charts():
    """示例1：生成所有可视化图表"""
    print("🎨 示例1：生成所有DRG可视化图表")
    print("-" * 50)
    
    try:
        # 导入可视化模块
        from drg_visualization import main
        
        # 生成所有图表
        main()
        print("✅ 所有图表生成完成！")
        
    except ImportError as e:
        print(f"❌ 导入错误：{e}")
        print("请确保已安装所需依赖：pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ 生成图表时出错：{e}")

def example_2_analyze_sample_data():
    """示例2：分析示例数据"""
    print("\n📊 示例2：分析示例数据")
    print("-" * 50)
    
    # 读取示例数据
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_data.txt')
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print("📋 示例数据分析：")
        case_count = 0
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                case_count += 1
                parts = line.split(',')
                if len(parts) >= 10:
                    case_id = parts[0]
                    age = parts[2]
                    gender = "女" if parts[1] == "2" else "男"
                    days = parts[6]
                    main_diag = parts[8].split('|')[0] if parts[8] else "无"
                    expected_drg = parts[10] if len(parts) > 10 else "未知"
                    
                    print(f"  病例{case_count}: {case_id} - {age}岁{gender}性，住院{days}天")
                    print(f"    主诊断: {main_diag}")
                    print(f"    预期分组: {expected_drg}")
                    print()
        
        print(f"📈 共找到 {case_count} 个示例病例")
        
    except FileNotFoundError:
        print(f"❌ 找不到数据文件：{data_file}")
    except Exception as e:
        print(f"❌ 分析数据时出错：{e}")

def example_3_explain_drg_concepts():
    """示例3：解释DRG核心概念"""
    print("\n📚 示例3：DRG核心概念解释")
    print("-" * 50)
    
    concepts = {
        "DRG": "疾病诊断相关组，用于医保按病种付费的分组方法",
        "MDC": "主要诊断大类，按人体系统分为26个大类（A-Z）",
        "ADRG": "核心DRG组，在MDC基础上按诊断和治疗方式细分",
        "MCC": "主要并发症或合并症，严重影响治疗复杂度的疾病",
        "CC": "并发症或合并症，一般性的合并疾病",
        "CCE": "并发症排除表，防止重复计算相关并发症"
    }
    
    for term, explanation in concepts.items():
        print(f"🔸 {term}: {explanation}")
    
    print("\n💡 分组逻辑：")
    print("   主诊断 → MDC → ADRG → 检查并发症 → 最终DRG")
    print("   例如：K22.301 → MDCG → GZ1 → 有CC → GZ13")

def example_4_drg_payment_impact():
    """示例4：DRG对医院支付的影响"""
    print("\n💰 示例4：DRG支付影响分析")
    print("-" * 50)
    
    # 模拟支付标准（仅供示例）
    payment_examples = [
        {"drg": "GZ11", "description": "其他消化诊断，伴严重并发症", "payment": 15000, "weight": 1.5},
        {"drg": "GZ13", "description": "其他消化诊断，伴并发症", "payment": 12000, "weight": 1.2},
        {"drg": "GZ15", "description": "其他消化诊断，不伴并发症", "payment": 8000, "weight": 0.8},
    ]
    
    print("📊 同一ADRG下不同DRG的支付差异：")
    for item in payment_examples:
        print(f"  {item['drg']}: {item['description']}")
        print(f"    支付标准: {item['payment']:,}元 (权重: {item['weight']})")
        print()
    
    print("💡 关键启示：")
    print("  • 准确的并发症编码直接影响医院收入")
    print("  • GZ11比GZ15高出87.5%的支付标准")
    print("  • 病案质量管理对医院经济效益至关重要")

def main():
    """主函数：运行所有示例"""
    print("🏥 DRG分组可视化学习指南 - 使用示例")
    print("=" * 60)
    
    # 运行所有示例
    example_1_generate_all_charts()
    example_2_analyze_sample_data()
    example_3_explain_drg_concepts()
    example_4_drg_payment_impact()
    
    print("\n🎓 学习建议：")
    print("1. 先查看HTML学习指南了解基础概念")
    print("2. 运行可视化脚本生成图表")
    print("3. 分析示例数据理解分组过程")
    print("4. 修改数据文件尝试不同的分组结果")
    
    print("\n📁 相关文件：")
    print("  • docs/drg_guide.html - 完整学习指南")
    print("  • images/*.png - 可视化图表")
    print("  • data/sample_data.txt - 示例数据")
    print("  • src/drg_visualization.py - 图表生成脚本")

if __name__ == "__main__":
    main()
