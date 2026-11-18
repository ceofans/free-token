"""Search the public CEOFans AI credit catalog. Requires Python 3.9+."""
import argparse
import json
import sys
from urllib.error import URLError
from urllib.request import Request, urlopen

CATALOG = "https://www.ceofans.com/api/free-tokens.php"
REGIONS = {"cn": "domestic", "intl": "international"}
OFFERS = {"recurring": "持续免费", "trial": "新人试用", "campaign": "限时活动", "conditional": "有条件优惠"}


def load_catalog():
    request = Request(CATALOG, headers={"Accept": "application/json", "User-Agent": "CEOFans-Free-Token-CLI"})
    with urlopen(request, timeout=15) as response:
        data = json.load(response)
    if not isinstance(data, dict) or data.get("schemaVersion") != 1 or not isinstance(data.get("items"), list):
        raise ValueError("目录格式无法识别")
    return data["items"]


def matches(item, args):
    if args.region and item.get("market") != REGIONS[args.region]:
        return False
    if args.no_card and item.get("cardRequired") != "no":
        return False
    fields = [item.get(key, "") for key in ("provider", "title", "summary")]
    fields += item.get("models", []) + item.get("tags", [])
    return args.search.casefold() in " ".join(fields).casefold()


def print_offer(item, details):
    kind = OFFERS.get(item.get("offerType"), "其他方案")
    print(f"[{kind}] {item['provider']} · {item['title']}")
    for label, field in (("额度", "quotaText"), ("条件", "requirements"), ("有效期", "validityText"),
                         ("核验日期", "verifiedAt"), ("申请入口", "claimUrl")):
        if item.get(field):
            print(f"  {label}  {item[field]}")
    if details:
        for n, step in enumerate(item.get("steps", []), 1):
            print(f"  {n}. {step['title']}  {step.get('body', '')}")
            if step.get("url"):
                print(f"     {step['url']}")
        if item.get("sourceUrl"):
            print(f"  官方出处  {item['sourceUrl']}")


def main():
    parser = argparse.ArgumentParser(description="查询国内外 AI 模型的免费额度和优惠")
    parser.add_argument("--region", choices=REGIONS, help="cn 国内，intl 国际，默认查询全部")
    parser.add_argument("--search", default="", help="厂商、模型或用途关键词")
    parser.add_argument("--no-card", action="store_true", help="仅显示已确认无需绑卡的方案")
    parser.add_argument("--details", action="store_true", help="显示官方出处和申请步骤")
    args = parser.parse_args()
    try:
        items = [item for item in load_catalog() if matches(item, args)]
    except (OSError, URLError, ValueError, KeyError, TypeError) as error:
        print(f"读取目录失败：{error}", file=sys.stderr)
        return 1
    print(f"找到 {len(items)} 个方案")
    for item in items:
        print()
        print_offer(item, args.details)
    return 0


if __name__ == "__main__":
    sys.exit(main())
