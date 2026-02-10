# VCEP 变异分类技能包

[English](./README.md) | 中文

一套用于遗传变异分类的 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 插件技能，基于 ACMG/AMP 标准和 ClinGen VCEP 规范。

## 包含技能

### variant-classifier（变异分类器）

使用 ACMG/AMP 标准对遗传变异进行分类，支持 ClinGen VCEP（变异解读专家组）基因特异性指南。

```
/variant-classifier "NM_000546.6:c.215C>G"
/variant-classifier rs1042522
/variant-classifier "chr17:7674220:C:T" --quick
```

功能：
- 自动 VEP 注释、gnomAD 频率查询、剪接预测
- 自动匹配 50+ 基因的 VCEP 规范
- 基于积分的分类系统（致病 / 可能致病 / 意义未明 / 可能良性 / 良性）
- 通过 PubMed/PMC 整合提取文献证据
- 生成带可视化的 HTML 报告
- 支持自定义备注和实验室政策（`--notes`、`--requirements`）

### vcep-spec（VCEP 规范下载器）

下载 ClinGen VCEP 规范文档并生成结构化的 Markdown 解读指南。

```
/vcep-spec GN101                    # 下载 + 生成指南
/vcep-spec GN147 --download-only   # 仅下载规范文件
/vcep-spec ./GN101-ACTC1           # 从已有文件夹生成
```

功能：
- 从 ClinGen 下载 PDF 规范、补充文件和元数据
- 读取 PDF、Excel、Word 和 PowerPoint 源文档
- 按标准化模板生成全面的 Markdown 指南
- 支持多基因和不同遗传模式的规范

### paper-finder（文献查找器）

通过 PMID 获取 PubMed 文章并提取原始全文内容。

```
/paper-finder 30128536 27720647 --metadata-only   # 快速预览
/paper-finder 30128536 -o ./papers                 # 获取全文
```

功能：
- 两步工作流：先预览元数据，再选择性获取全文
- 从 PubMed 抓取元数据/摘要，从 PMC 抓取全文
- 结构化 Markdown 输出，包含章节、表格和参考文献

## 安装

### 前置要求

- 已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- Python 3.7+
- Python 依赖包：`requests`、`beautifulsoup4`

```bash
pip install requests beautifulsoup4
```

### 通过插件市场安装（推荐）

1. 在 Claude Code 中添加市场：

```
/plugin marketplace add muwenbo/vcep-classification-skills
```

2. 安装所需插件：

```
/plugin install variant-classifier@vcep-classification-skills
/plugin install vcep-spec@vcep-classification-skills
/plugin install paper-finder@vcep-classification-skills
```

3. 验证安装 - 技能将显示为可用的斜杠命令：

```
/variant-classifier
/vcep-spec
/paper-finder
```

### 更新

更新市场以获取最新版本：

```
/plugin marketplace update vcep-classification-skills
```

### 手动安装（备选方式）

也可以克隆仓库后本地添加：

```bash
git clone https://github.com/muwenbo/vcep-classification-skills.git
```

```
/plugin marketplace add ./vcep-classification-skills
/plugin install variant-classifier@vcep-classification-skills
```

## 使用方法

安装完成后，在 Claude Code 中使用斜杠命令调用技能：

```
> /variant-classifier "NM_000546.6:c.215C>G"
> /vcep-spec GN101
> /paper-finder 30128536
```

各技能的详细用法请参阅各插件 `skills/` 目录下的 `SKILL.md` 文件。

## 许可证

MIT
