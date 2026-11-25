"""共用設定：路徑、中文字型、洲別對照表。"""
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "covid_vaccination_vs_death_ratio.csv"
PROCESSED = ROOT / "data" / "processed"
FIG = ROOT / "figures"
RESULTS = ROOT / "results"
for p in (PROCESSED, FIG, RESULTS):
    p.mkdir(parents=True, exist_ok=True)

RANDOM_STATE = 42


FONT_FILE = ROOT / "fonts" / "FGroupCJK-Regular.otf"


def setup_font():
    """設定繁體中文字型。
    優先用專案內建字型 fonts/FGroupCJK-Regular.otf（Noto Sans CJK TC 子集），
    不論 Windows、Mac、Colab 或 GitHub Codespaces，不用另外安裝就能顯示中文；
    內建字型沒有的字，再依序找系統字型。
    """
    names = []
    if FONT_FILE.exists():
        font_manager.fontManager.addfont(str(FONT_FILE))
        names.append(font_manager.FontProperties(fname=str(FONT_FILE)).get_name())
    installed = {f.name for f in font_manager.fontManager.ttflist}
    names += [n for n in ["Microsoft JhengHei", "PingFang TC", "Heiti TC", "Noto Sans CJK TC",
                          "Noto Sans TC", "Arial Unicode MS"] if n in installed]
    if not names:
        print("警告：找不到中文字型，圖上的中文會變成方框。請確認 fonts/ 資料夾有一起上傳。")
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = names + ["DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["figure.dpi"] = 110
    plt.rcParams["savefig.dpi"] = 150
    plt.rcParams["savefig.bbox"] = "tight"
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False


# 洲別對照（依 Our World in Data 的分類；資料本身沒有洲別欄位，用 ISO 代碼對照）
CONTINENT_ISO = {
    "亞洲": "AFG ARE ARM AZE BGD BHR BRN BTN CHN GEO IDN IND IRN IRQ ISR JOR JPN KAZ KGZ KHM KOR KWT LAO "
            "LBN LKA MDV MMR MNG MYS NPL OMN PAK PHL PSE QAT SAU SGP SYR THA TJK TKM TUR UZB VNM YEM",
    "歐洲": "ALB AND AUT BEL BGR BIH BLR CHE CYP DEU DNK ESP EST FIN FRA GBR GIB GRC HRV HUN IMN IRL ISL ITA "
            "LIE LTU LUX LVA MCO MDA MKD MLT MNE NLD NOR POL PRT ROU RUS SMR SRB SVK SVN SWE UKR",
    "非洲": "AGO BEN BFA BWA CAF CMR COM CPV DJI DZA EGY ETH GAB GHA GIN GMB GNB GNQ KEN LBR LBY LSO MAR MDG "
            "MLI MOZ MRT MUS MWI NAM NER NGA RWA SDN SEN SLE SOM SSD STP SYC TCD TGO TUN TZA UGA ZAF ZMB ZWE",
    "北美洲": "ABW AIA ATG BHS BLZ BMU BRB CAN CRI CUB CUW CYM DMA DOM GRD GRL GTM HND HTI JAM KNA LCA MEX MSR "
             "NIC PAN SLV TCA TTO USA VCT",
    "南美洲": "ARG BOL BRA CHL COL ECU FLK GUY PER PRY SUR URY VEN",
    "大洋洲": "AUS COK FJI KIR NCL NIU NRU NZL PNG PYF SLB TKL TON TUV VUT WLF WSM",
}
ISO_TO_CONTINENT = {iso: c for c, codes in CONTINENT_ISO.items() for iso in codes.split()}

CONTINENT_COLORS = {
    "亞洲": "#d1495b", "歐洲": "#00798c", "非洲": "#edae49",
    "北美洲": "#30638e", "南美洲": "#66a182", "大洋洲": "#8d6a9f",
}
