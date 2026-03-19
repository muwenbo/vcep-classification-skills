# VCEP 变异分类技能包

[English](./README.md) | 中文

AI 编程代理技能包，用于基于 ACMG/AMP 标准和 ClinGen VCEP 规范的遗传变异分类。兼容任何支持技能/插件格式的代理（Claude Code、Gemini CLI 等）。

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

- 支持技能/插件格式的 AI 编程代理（如 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)、[Gemini CLI](https://github.com/google-gemini/gemini-cli)）
- Python 3.7+
- Python 依赖包：`requests`、`beautifulsoup4`

```bash
pip install requests beautifulsoup4
```

### 通过插件市场安装

**Claude Code：**

```
/plugin marketplace add muwenbo/vcep-classification-skills
/plugin install variant-classifier@vcep-classification-skills
/plugin install vcep-spec@vcep-classification-skills
/plugin install paper-finder@vcep-classification-skills
```

**其他代理：** 克隆仓库后将代理指向 `plugins/` 目录或各技能文件夹：

```bash
git clone https://github.com/muwenbo/vcep-classification-skills.git
```

每个技能独立存放于 `plugins/<skill>/skills/<skill>/`，以 `SKILL.md` 为入口。

### 更新

**Claude Code：**

```
/plugin marketplace update vcep-classification-skills
```

**其他代理：** 运行 `git pull` 获取最新版本。

## 使用方法

通过斜杠命令或直接向代理提问来调用技能：

```
/variant-classifier "NM_000546.6:c.215C>G"
/vcep-spec GN101
/paper-finder 30128536
```

各技能的详细用法请参阅各插件 `skills/` 目录下的 `SKILL.md` 文件。

## 许可证

MIT
