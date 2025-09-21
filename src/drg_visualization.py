#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DRG分组可视化工具
帮助理解DRG分组的业务逻辑和流程
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import pandas as pd

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def create_drg_overview_flowchart():
    """创建DRG分组总体流程图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # 定义颜色
    colors = {
        'input': '#E3F2FD',
        'process': '#BBDEFB', 
        'decision': '#90CAF9',
        'output': '#64B5F6',
        'final': '#42A5F5'
    }
    
    # 绘制流程图
    boxes = [
        # 输入阶段
        {'xy': (1, 10.5), 'width': 2, 'height': 1, 'text': '病人入院\n基本信息', 'color': colors['input']},
        {'xy': (4, 10.5), 'width': 2, 'height': 1, 'text': '医疗记录\n诊断&手术', 'color': colors['input']},
        {'xy': (7, 10.5), 'width': 2, 'height': 1, 'text': '出院信息\n住院天数等', 'color': colors['input']},
        
        # 处理阶段
        {'xy': (4, 9), 'width': 2, 'height': 1, 'text': '数据预处理\n格式转换', 'color': colors['process']},
        {'xy': (4, 7.5), 'width': 2, 'height': 1, 'text': '信息校验\n完整性检查', 'color': colors['process']},
        
        # 分组阶段
        {'xy': (4, 6), 'width': 2, 'height': 1, 'text': 'MDC分类\n按系统分组', 'color': colors['decision']},
        {'xy': (4, 4.5), 'width': 2, 'height': 1, 'text': 'ADRG细分\n核心组划分', 'color': colors['decision']},
        {'xy': (4, 3), 'width': 2, 'height': 1, 'text': 'DRG最终分组\n并发症判断', 'color': colors['decision']},
        
        # 输出阶段
        {'xy': (4, 1.5), 'width': 2, 'height': 1, 'text': '分组结果\n权重&支付标准', 'color': colors['final']},
    ]
    
    # 绘制方框
    for box in boxes:
        rect = FancyBboxPatch(
            box['xy'], box['width'], box['height'],
            boxstyle="round,pad=0.1",
            facecolor=box['color'],
            edgecolor='black',
            linewidth=1
        )
        ax.add_patch(rect)
        
        # 添加文本
        ax.text(
            box['xy'][0] + box['width']/2, 
            box['xy'][1] + box['height']/2,
            box['text'], 
            ha='center', va='center', 
            fontsize=10, fontweight='bold'
        )
    
    # 绘制箭头
    arrows = [
        ((2, 10.5), (4, 10.5)),  # 基本信息 -> 医疗记录
        ((6, 10.5), (7, 10.5)),  # 医疗记录 -> 出院信息
        ((5, 10.5), (5, 9.5)),   # 输入 -> 预处理
        ((5, 9), (5, 8.5)),      # 预处理 -> 校验
        ((5, 7.5), (5, 7)),      # 校验 -> MDC
        ((5, 6), (5, 5.5)),      # MDC -> ADRG
        ((5, 4.5), (5, 4)),      # ADRG -> DRG
        ((5, 3), (5, 2.5)),      # DRG -> 结果
    ]
    
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    # 添加侧边说明
    side_notes = [
        {'pos': (0.5, 8), 'text': '数据\n准备', 'color': colors['input']},
        {'pos': (0.5, 5), 'text': '分组\n逻辑', 'color': colors['decision']},
        {'pos': (0.5, 1.5), 'text': '最终\n结果', 'color': colors['final']},
    ]
    
    for note in side_notes:
        rect = FancyBboxPatch(
            (note['pos'][0]-0.3, note['pos'][1]-0.5), 0.6, 1,
            boxstyle="round,pad=0.05",
            facecolor=note['color'],
            edgecolor='gray',
            linewidth=1
        )
        ax.add_patch(rect)
        ax.text(note['pos'][0], note['pos'][1], note['text'], 
               ha='center', va='center', fontsize=8, fontweight='bold')
    
    plt.title('DRG分组总体流程图', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_three_level_structure():
    """创建三层分组结构图"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # MDC层 (顶层)
    mdc_examples = ['MDCA\n神经系统', 'MDCE\n循环系统', 'MDCG\n消化系统', 'MDCJ\n皮肤系统', 'MDCL\n肌肉骨骼']
    mdc_colors = ['#FFE0B2', '#F3E5F5', '#E8F5E8', '#FFF3E0', '#E1F5FE']
    
    for i, (mdc, color) in enumerate(zip(mdc_examples, mdc_colors)):
        rect = FancyBboxPatch(
            (i*3 + 0.5, 8), 2.5, 1.2,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor='black',
            linewidth=2
        )
        ax.add_patch(rect)
        ax.text(i*3 + 1.75, 8.6, mdc, ha='center', va='center', 
               fontsize=10, fontweight='bold')
    
    # ADRG层 (中层) - 以MDCG为例
    adrg_examples = ['GB1\n胰肝手术', 'GC1\n胆道手术', 'GZ1\n其他诊断']
    adrg_y = 5.5
    
    for i, adrg in enumerate(adrg_examples):
        rect = FancyBboxPatch(
            (6 + i*2, adrg_y), 1.8, 1,
            boxstyle="round,pad=0.1",
            facecolor='#E8F5E8',
            edgecolor='green',
            linewidth=1.5
        )
        ax.add_patch(rect)
        ax.text(6 + i*2 + 0.9, adrg_y + 0.5, adrg, ha='center', va='center', 
               fontsize=9, fontweight='bold')
    
    # DRG层 (底层) - 以GZ1为例
    drg_examples = ['GZ11\n伴严重并发症', 'GZ13\n伴并发症', 'GZ15\n不伴并发症']
    drg_colors = ['#FFCDD2', '#FFE0B2', '#C8E6C9']
    drg_y = 2.5
    
    for i, (drg, color) in enumerate(zip(drg_examples, drg_colors)):
        rect = FancyBboxPatch(
            (8 + i*2, drg_y), 1.8, 1,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor='red' if '11' in drg else 'orange' if '13' in drg else 'green',
            linewidth=1.5
        )
        ax.add_patch(rect)
        ax.text(8 + i*2 + 0.9, drg_y + 0.5, drg, ha='center', va='center', 
               fontsize=9, fontweight='bold')
    
    # 绘制连接线
    # MDC到ADRG
    ax.annotate('', xy=(7.5, 6.5), xytext=(7.5, 8),
               arrowprops=dict(arrowstyle='->', lw=2, color='green'))
    
    # ADRG到DRG
    for i in range(3):
        ax.annotate('', xy=(9 + i*2, 3.5), xytext=(9, 5.5),
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='red'))
    
    # 添加层级标签
    ax.text(0.2, 8.6, 'MDC层\n(26个大类)', ha='left', va='center', 
           fontsize=12, fontweight='bold', color='blue')
    ax.text(0.2, 6, 'ADRG层\n(核心组)', ha='left', va='center', 
           fontsize=12, fontweight='bold', color='green')
    ax.text(0.2, 3, 'DRG层\n(最终分组)', ha='left', va='center', 
           fontsize=12, fontweight='bold', color='red')
    
    # 添加说明文字
    ax.text(8, 0.5, '支付标准: GZ11 > GZ13 > GZ15', ha='center', va='center',
           fontsize=11, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", 
           facecolor='yellow', alpha=0.7))
    
    plt.title('DRG三层分组结构图', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_cc_logic_flowchart():
    """创建并发症判断逻辑流程图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # 定义决策节点
    nodes = [
        {'pos': (7, 11), 'text': '开始\n病人有多个诊断？', 'shape': 'diamond', 'color': '#FFE0B2'},
        {'pos': (3, 9.5), 'text': '只有主诊断\n分入15组\n(不伴并发症)', 'shape': 'rect', 'color': '#C8E6C9'},
        {'pos': (7, 9), 'text': '获取主诊断的\n排除表(CCE)', 'shape': 'rect', 'color': '#E3F2FD'},
        {'pos': (7, 7.5), 'text': '遍历其他诊断\n检查是否为MCC', 'shape': 'rect', 'color': '#E3F2FD'},
        {'pos': (3, 6), 'text': '是MCC且\n不在排除表？', 'shape': 'diamond', 'color': '#FFF3E0'},
        {'pos': (1, 4.5), 'text': '分入11组\n(伴严重并发症)', 'shape': 'rect', 'color': '#FFCDD2'},
        {'pos': (7, 4.5), 'text': '检查是否为CC', 'shape': 'rect', 'color': '#E3F2FD'},
        {'pos': (11, 6), 'text': '是CC且\n不在排除表？', 'shape': 'diamond', 'color': '#F3E5F5'},
        {'pos': (13, 4.5), 'text': '分入13组\n(伴并发症)', 'shape': 'rect', 'color': '#FFE0B2'},
        {'pos': (7, 2), 'text': '分入15组\n(不伴并发症)', 'shape': 'rect', 'color': '#C8E6C9'},
    ]
    
    # 绘制节点
    for node in nodes:
        if node['shape'] == 'diamond':
            # 菱形决策节点
            diamond = patches.RegularPolygon(
                node['pos'], 4, radius=0.8, orientation=np.pi/4,
                facecolor=node['color'], edgecolor='black', linewidth=1.5
            )
            ax.add_patch(diamond)
        else:
            # 矩形处理节点
            rect = FancyBboxPatch(
                (node['pos'][0]-0.8, node['pos'][1]-0.4), 1.6, 0.8,
                boxstyle="round,pad=0.1",
                facecolor=node['color'],
                edgecolor='black',
                linewidth=1.5
            )
            ax.add_patch(rect)
        
        ax.text(node['pos'][0], node['pos'][1], node['text'], 
               ha='center', va='center', fontsize=9, fontweight='bold')
    
    # 绘制连接线和标签
    connections = [
        ((7, 10.2), (3, 10), '否'),
        ((7, 10.2), (7, 9.5), '是'),
        ((7, 8.5), (7, 8), ''),
        ((7, 7), (3, 6.5), ''),
        ((3, 5.2), (1, 5), '是'),
        ((3, 5.2), (7, 5), '否'),
        ((7, 4), (11, 6.5), ''),
        ((11, 5.2), (13, 5), '是'),
        ((11, 5.2), (7, 2.5), '否'),
    ]
    
    for connection in connections:
        start, end, label = connection
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
        if label:
            mid_x, mid_y = (start[0] + end[0])/2, (start[1] + end[1])/2
            ax.text(mid_x, mid_y, label, ha='center', va='center',
                   fontsize=8, fontweight='bold', 
                   bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
    
    # 添加示例说明
    example_text = """
    示例说明：
    主诊断：K22.301 (食管破裂) - 排除表111
    其他诊断：
    • K11.901 (腮腺区肿物) - CC，排除表110 ✓
    • E11.900 (2型糖尿病) - CC，排除表110 ✓  
    • I10.x05 (高血压3级) - CC，排除表110 ✓
    
    结果：有CC且不在同一排除表 → GZ13
    """
    
    ax.text(0.5, 1, example_text, ha='left', va='bottom', fontsize=9,
           bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.8))
    
    plt.title('DRG并发症判断逻辑流程图', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_case_analysis_chart():
    """创建具体病例分析图"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # 左图：病例信息展示
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('病例信息分析', fontsize=14, fontweight='bold')
    
    # 病例基本信息
    case_info = [
        ('病案号', '22058878'),
        ('性别', '女 (2)'),
        ('年龄', '88岁'),
        ('住院天数', '94天'),
        ('主诊断', 'K22.301 食管破裂'),
        ('其他诊断', 'K11.901 腮腺区肿物'),
        ('', 'E11.900 2型糖尿病'),
        ('', 'I10.x05 高血压3级'),
        ('手术操作', '96.0800x005 鼻十二指肠营养管置入术'),
    ]
    
    for i, (label, value) in enumerate(case_info):
        y_pos = 9 - i * 0.8
        if label:
            ax1.text(0.5, y_pos, f'{label}:', ha='left', va='center', 
                    fontsize=11, fontweight='bold')
            ax1.text(3.5, y_pos, value, ha='left', va='center', fontsize=11)
        else:
            ax1.text(3.5, y_pos, value, ha='left', va='center', fontsize=11, color='blue')
    
    # 右图：分组过程
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('分组决策过程', fontsize=14, fontweight='bold')
    
    # 分组步骤
    steps = [
        ('1. MDC判断', 'K22.301属于消化系统 → MDCG', '#E8F5E8'),
        ('2. ADRG判断', 'K22.301属于其他消化诊断 → GZ1', '#E3F2FD'),
        ('3. CC/MCC检查', '检查其他诊断的并发症属性', '#FFF3E0'),
        ('   K11.901', '腮腺区肿物 → CC (排除表110)', '#FFE0B2'),
        ('   E11.900', '2型糖尿病 → CC (排除表110)', '#FFE0B2'),
        ('   I10.x05', '高血压3级 → CC (排除表110)', '#FFE0B2'),
        ('4. 排除表检查', '主诊断排除表111 ≠ CC排除表110', '#F3E5F5'),
        ('5. 最终分组', 'GZ13 - 其他消化系统诊断，伴并发症', '#FFCDD2'),
    ]
    
    for i, (step, desc, color) in enumerate(steps):
        y_pos = 9.5 - i * 0.9
        
        # 绘制背景框
        rect = FancyBboxPatch(
            (0.2, y_pos - 0.3), 9.6, 0.6,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor='gray',
            linewidth=1,
            alpha=0.7
        )
        ax2.add_patch(rect)
        
        ax2.text(0.5, y_pos, step, ha='left', va='center', 
                fontsize=10, fontweight='bold')
        ax2.text(2.8, y_pos, desc, ha='left', va='center', fontsize=10)
    
    plt.tight_layout()
    return fig

def main():
    """主函数：生成所有可视化图表"""
    print("正在生成DRG分组可视化图表...")
    
    # 1. 总体流程图
    fig1 = create_drg_overview_flowchart()
    fig1.savefig('drg_overview_flowchart.png', dpi=300, bbox_inches='tight')
    print("✓ 已生成：drg_overview_flowchart.png")
    
    # 2. 三层结构图
    fig2 = create_three_level_structure()
    fig2.savefig('drg_three_level_structure.png', dpi=300, bbox_inches='tight')
    print("✓ 已生成：drg_three_level_structure.png")
    
    # 3. 并发症判断逻辑图
    fig3 = create_cc_logic_flowchart()
    fig3.savefig('drg_cc_logic_flowchart.png', dpi=300, bbox_inches='tight')
    print("✓ 已生成：drg_cc_logic_flowchart.png")
    
    # 4. 具体病例分析图
    fig4 = create_case_analysis_chart()
    fig4.savefig('drg_case_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ 已生成：drg_case_analysis.png")
    
    print("\n所有图表已生成完成！")
    print("你可以查看以下文件来理解DRG分组：")
    print("1. drg_overview_flowchart.png - DRG分组总体流程")
    print("2. drg_three_level_structure.png - 三层分组结构")
    print("3. drg_cc_logic_flowchart.png - 并发症判断逻辑")
    print("4. drg_case_analysis.png - 具体病例分析")

if __name__ == "__main__":
    main()
