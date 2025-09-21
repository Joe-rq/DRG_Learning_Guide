# 🏥 DRG分组可视化学习指南

## 项目简介

这是一个专门用于学习和理解DRG（疾病诊断相关组）分组逻辑的可视化教学项目。通过图形化的方式展示DRG分组的业务流程、技术实现和实际应用，帮助医疗信息化从业者、医院管理人员和相关学习者快速掌握DRG分组的核心概念。

## 🎯 项目特色

- **📊 可视化图表**：4个专业的流程图和结构图
- **📚 详细文档**：完整的HTML学习指南
- **💻 源代码**：Python可视化生成脚本
- **📋 实例分析**：真实病例的分组过程演示
- **🔧 可扩展**：易于修改和扩展的代码结构

## 📁 项目结构

```
DRG_Learning_Guide/
├── README.md                   # 项目说明文档
├── requirements.txt            # Python依赖包
├── docs/                       # 文档目录
│   └── drg_guide.html         # HTML学习指南
├── images/                     # 图表文件
│   ├── drg_overview_flowchart.png      # DRG分组总体流程图
│   ├── drg_three_level_structure.png   # 三层分组结构图
│   ├── drg_cc_logic_flowchart.png      # 并发症判断逻辑图
│   └── drg_case_analysis.png           # 具体病例分析图
├── src/                        # 源代码目录
│   └── drg_visualization.py   # 可视化生成脚本
├── data/                       # 数据目录
│   └── sample_data.txt        # 示例数据
└── examples/                   # 示例目录
    └── usage_examples.py      # 使用示例
```

## 🚀 快速开始

### 1. 环境准备

确保你的系统已安装Python 3.8+，推荐使用虚拟环境：

```bash
# 使用uv创建虚拟环境（推荐）
uv venv
source .venv/bin/activate  # Linux/Mac
# 或者 .venv\Scripts\activate  # Windows

# 或使用传统方式
python -m venv venv
source venv/bin/activate
```

### 2. 安装依赖

```bash
# 使用uv安装（推荐）
uv run --with matplotlib --with pandas --with numpy python src/drg_visualization.py

# 或使用pip安装
pip install -r requirements.txt
```

### 3. 生成图表

```bash
# 运行可视化脚本
python src/drg_visualization.py
```

### 4. 查看学习指南

在浏览器中打开 `docs/drg_guide.html` 文件，开始你的DRG学习之旅！

## 📊 图表说明

### 1. DRG分组总体流程图
- **文件**: `images/drg_overview_flowchart.png`
- **内容**: 从病人入院到最终分组的完整流程
- **用途**: 理解DRG分组的整体业务逻辑

### 2. 三层分组结构图
- **文件**: `images/drg_three_level_structure.png`
- **内容**: MDC → ADRG → DRG的层次关系
- **用途**: 掌握分组的层次结构和分类原理

### 3. 并发症判断逻辑图
- **文件**: `images/drg_cc_logic_flowchart.png`
- **内容**: MCC/CC并发症的判断决策树
- **用途**: 理解最终分组的核心判断逻辑

### 4. 具体病例分析图
- **文件**: `images/drg_case_analysis.png`
- **内容**: 真实病例的完整分组过程
- **用途**: 通过实例加深理解

## 🎓 学习路径

1. **基础概念** → 阅读HTML指南中的基础概念部分
2. **流程理解** → 查看总体流程图，理解分组步骤
3. **结构掌握** → 学习三层结构图，掌握分组层次
4. **逻辑深入** → 研究并发症判断逻辑，理解核心算法
5. **实例应用** → 分析具体病例，巩固学习成果
6. **代码实践** → 阅读源代码，了解技术实现

## 💡 核心概念

### DRG分组的三个层次：
- **MDC（主要诊断大类）**: 按人体系统分为26个大类
- **ADRG（核心DRG组）**: 按诊断和治疗方式细分
- **DRG（最终分组）**: 按并发症严重程度分为1/3/5组

### 关键判断因素：
- **主诊断**: 决定MDC分类
- **手术操作**: 影响ADRG选择
- **并发症/合并症**: 决定最终DRG分组
- **年龄、性别**: 特定情况下的修正因素

## 🔧 自定义和扩展

### 修改图表样式
编辑 `src/drg_visualization.py` 中的颜色和布局设置：

```python
colors = {
    'input': '#E3F2FD',    # 输入阶段颜色
    'process': '#BBDEFB',  # 处理阶段颜色
    'decision': '#90CAF9', # 决策阶段颜色
    # ... 更多自定义选项
}
```

### 添加新的病例分析
1. 在 `data/sample_data.txt` 中添加新的病例数据
2. 修改 `create_case_analysis_chart()` 函数
3. 重新生成图表

### 扩展学习内容
1. 编辑 `docs/drg_guide.html` 添加新的章节
2. 创建新的可视化图表
3. 更新README文档

## 📚 相关资源

- [国家医保局DRG官方文档](http://www.nhsa.gov.cn/)
- [ICD-10疾病诊断编码](https://icd.who.int/browse10/2019/en)
- [DRG支付方式改革政策解读](http://www.nhsa.gov.cn/)

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目：

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 📧 Email: qrq-hit@foxmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/Joe-rq/DRG_Learning_Guide/issues)
- 🌐 项目地址: [https://github.com/Joe-rq/DRG_Learning_Guide](https://github.com/Joe-rq/DRG_Learning_Guide)

## 🙏 致谢

感谢所有为DRG分组标准制定和实施做出贡献的医疗信息化专家和从业者。

---

⭐ 如果这个项目对你有帮助，请给它一个Star！
