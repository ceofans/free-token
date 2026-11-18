# 全球免费 Token · CEOFans

一个查询 AI 模型官方免费额度和优惠的命令行小工具。输入厂商名，查看可领取的额度、申请条件、有效期、最近核验日期和官方入口。目录由 CEOFans 维护。

## 快速开始

安装 Python 3.9 或更高版本，在本目录运行以下命令。仅使用 Python 标准库。

```sh
python free_token.py --region cn --search 小米
python free_token.py --region intl --no-card
python free_token.py --search Gemini --details
```

每次运行发起一次公开目录读取请求，筛选在本机完成。`--no-card` 仅包含已确认无需绑卡的方案。`--details` 展示申请步骤和官方出处。试用、限时活动和需要付费才能享受的优惠会分别标明，实际资格和价格以厂商页面为准。

## CEOFans 账号和免费模型

查询目录无需登录，也无需输入 API Key。想使用 CEOFans 自营模型，可在官方 Windows 桌面版登录自己的老板账号，按照应用显示的规则手动领取当日积分，再通过自己的模型 Key 使用服务。奖励归属各自账户，积分以服务器账本为准，模型调用会按当期规则消耗积分。第三方厂商的赠额请在该厂商的官方页面领取。[下载官方桌面版](https://www.ceofans.com/free-token/?utm_source=github&utm_medium=readme)

本仓库的代码范围为只读命令行工具。桌面端、账号服务、积分账本及模型网关由 CEOFans 独立提供。提交问题时请给出方案名、官方链接和核验日期，截图中请遮住账号和密钥。

[了解 CEOFans](https://www.ceofans.com/)
