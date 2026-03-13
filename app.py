from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ============================================================
#  시드니 데이터 - 맛집 / 관광지 / 꿀팁
# ============================================================

RESTAURANTS = [
    {
        "id": 1,
        "name": "Bourke Street Bakery",
        "category": "카페/베이커리",
        "area": "Surry Hills",
        "price": "$$",
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600",
        "desc": "시드니 로컬들이 사랑하는 베이커리. 소시지 롤과 사워도우가 필수!",
        "tip": "주말 아침엔 줄이 길어요. 평일 오전 추천!",
        "tags": ["브런치", "빵", "커피"],
        "coords": {"lat": -33.885, "lng": 151.211}
    },
    {
        "id": 2,
        "name": "Chin Chin Sydney",
        "category": "아시안",
        "area": "Surry Hills",
        "price": "$$$",
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1562967916-eb82221dfb44?w=600",
        "desc": "태국/동남아 퓨전. 분위기 좋고 음식 맛있기로 유명.",
        "tip": "예약 필수! 워크인은 대기가 길 수 있어요.",
        "tags": ["아시안", "퓨전", "디너"],
        "coords": {"lat": -33.884, "lng": 151.210}
    },
    {
        "id": 3,
        "name": "The Grounds of Alexandria",
        "category": "카페/브런치",
        "area": "Alexandria",
        "price": "$$",
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=600",
        "desc": "시드니에서 가장 인스타그래머블한 카페! 정원이 동화 속 같아요.",
        "tip": "주말은 인파가 어마어마해요. 오픈 시간에 맞춰 가세요!",
        "tags": ["인스타", "브런치", "정원"],
        "coords": {"lat": -33.910, "lng": 151.194}
    },
    {
        "id": 4,
        "name": "Quay Restaurant",
        "category": "파인다이닝",
        "area": "The Rocks",
        "price": "$$$$",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600",
        "desc": "오페라하우스 뷰 + 세계적 수준의 요리. 특별한 날에 완벽.",
        "tip": "코스 메뉴만 있어요. 예산 넉넉히 준비! 런치가 상대적으로 저렴.",
        "tags": ["파인다이닝", "뷰맛집", "특별한날"],
        "coords": {"lat": -33.858, "lng": 151.209}
    },
    {
        "id": 5,
        "name": "Mamak",
        "category": "아시안",
        "area": "Chinatown",
        "price": "$",
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=600",
        "desc": "말레이시안 스트리트 푸드. 로티 차나이가 미쳐요!",
        "tip": "항상 줄 서지만 회전이 빨라요. 로티 + 사테이 조합 강추!",
        "tags": ["말레이시안", "저렴한", "줄서는맛집"],
        "coords": {"lat": -33.878, "lng": 151.205}
    },
    {
        "id": 6,
        "name": "Bennelong",
        "category": "모던오지",
        "area": "Circular Quay",
        "price": "$$$$",
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1550966871-3ed3cdb51f3a?w=600",
        "desc": "오페라하우스 안에 있는 레스토랑! 호주 식재료로 만든 요리.",
        "tip": "프리시어터 메뉴가 가성비 좋아요. 공연 전 디너로 딱!",
        "tags": ["오페라하우스", "모던호주", "특별한날"],
        "coords": {"lat": -33.857, "lng": 151.215}
    },
    {
        "id": 7,
        "name": "Pancakes on the Rocks",
        "category": "카페/디저트",
        "area": "The Rocks",
        "price": "$",
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=600",
        "desc": "24시간 팬케이크 맛집! 달달한 게 당길 때 최고.",
        "tip": "Devil's Delight 팬케이크 꼭 먹어봐야 해요!",
        "tags": ["24시간", "디저트", "팬케이크"],
        "coords": {"lat": -33.859, "lng": 151.208}
    },
    {
        "id": 8,
        "name": "Fish Market (시드니 피쉬마켓)",
        "category": "해산물",
        "area": "Pyrmont",
        "price": "$$",
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1559737558-2f5a35f4523b?w=600",
        "desc": "세계 3대 fish market! 신선한 해산물을 그 자리에서.",
        "tip": "오전에 가야 신선해요. 갈매기 조심! 실내에서 먹는 걸 추천.",
        "tags": ["해산물", "시장", "런치"],
        "coords": {"lat": -33.870, "lng": 151.192}
    },
    {
        "id": 9,
        "name": "Barangaroo House",
        "category": "모던오지",
        "area": "Barangaroo",
        "price": "$$$",
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600",
        "desc": "3층짜리 복합 다이닝. 루프탑 바에서 보는 하버 뷰가 미쳤어요.",
        "tip": "1층은 캐주얼, 2층은 레스토랑, 3층은 바. 선셋 타임 루프탑 강추!",
        "tags": ["루프탑", "바", "하버뷰"],
        "coords": {"lat": -33.861, "lng": 151.201}
    },
    {
        "id": 10,
        "name": "Harry's Cafe de Wheels",
        "category": "스트리트푸드",
        "area": "Woolloomooloo",
        "price": "$",
        "rating": 4.2,
        "image": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=600",
        "desc": "1938년부터 이어온 전설의 미트파이! 호주 문화 체험 필수.",
        "tip": "Tiger Pie(카레 파이) 추천! 작은 가게지만 역사가 깊어요.",
        "tags": ["호주음식", "미트파이", "역사"],
        "coords": {"lat": -33.867, "lng": 151.222}
    },
]

ATTRACTIONS = [
    {
        "id": 1,
        "name": "Sydney Opera House",
        "category": "랜드마크",
        "area": "Circular Quay",
        "image": "https://images.unsplash.com/photo-1524293581917-878a6d017c71?w=600",
        "desc": "시드니의 상징! 외관도 멋지지만 내부 투어도 강력 추천.",
        "tip": "밤에 조명 라이트업이 진짜 예뻐요. 선셋~야경 시간대 추천!",
        "duration": "1-2시간",
        "cost": "외관 무료 / 투어 $43~",
        "tags": ["필수", "야경", "문화"]
    },
    {
        "id": 2,
        "name": "Harbour Bridge",
        "category": "랜드마크",
        "area": "The Rocks",
        "image": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=600",
        "desc": "걸어서 건너도 좋고, 꼭대기까지 클라이밍하면 잊을 수 없는 경험!",
        "tip": "Bridge Climb은 비싸지만 인생 경험. 걷기만 해도 충분히 좋아요.",
        "duration": "도보 30분 / 클라임 3시간",
        "cost": "도보 무료 / 클라임 $174~",
        "tags": ["필수", "뷰", "액티비티"]
    },
    {
        "id": 3,
        "name": "Bondi Beach",
        "category": "비치",
        "area": "Bondi",
        "image": "https://images.unsplash.com/photo-1578946956088-940c3b502864?w=600",
        "desc": "세계에서 가장 유명한 해변 중 하나. 서핑, 수영, 산책 다 가능!",
        "tip": "Bondi to Coogee 해안 산책로(6km)가 시드니 최고의 워킹 코스!",
        "duration": "반나절~하루",
        "cost": "무료",
        "tags": ["필수", "비치", "산책"]
    },
    {
        "id": 4,
        "name": "The Rocks",
        "category": "동네탐방",
        "area": "The Rocks",
        "image": "https://images.unsplash.com/photo-1549180030-48bf079fb38a?w=600",
        "desc": "시드니에서 가장 오래된 동네. 주말 마켓, 갤러리, 펍이 가득.",
        "tip": "토~일 The Rocks Markets 꼭 가세요! 핸드메이드 기념품 쇼핑 최고.",
        "duration": "2-3시간",
        "cost": "무료 (쇼핑 별도)",
        "tags": ["마켓", "쇼핑", "역사"]
    },
    {
        "id": 5,
        "name": "Royal Botanic Garden",
        "category": "자연",
        "area": "CBD",
        "image": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=600",
        "desc": "도심 속 거대한 정원. 오페라하우스 뷰포인트 Mrs Macquarie's Chair 포함!",
        "tip": "Mrs Macquarie's Chair에서 오페라하우스+하버브릿지 투샷 가능!",
        "duration": "1-2시간",
        "cost": "무료",
        "tags": ["무료", "자연", "포토스팟"]
    },
    {
        "id": 6,
        "name": "Taronga Zoo",
        "category": "체험",
        "area": "Mosman",
        "image": "https://images.unsplash.com/photo-1459262838948-3e2de6c1ec80?w=600",
        "desc": "하버 뷰 동물원! 코알라, 캥거루 등 호주 동물 만남.",
        "tip": "Circular Quay에서 페리로 12분! 페리 타는 것 자체가 관광.",
        "duration": "반나절",
        "cost": "$51 (온라인 할인)",
        "tags": ["동물", "페리", "가족"]
    },
    {
        "id": 7,
        "name": "Manly Beach",
        "category": "비치",
        "area": "Manly",
        "price": "무료",
        "image": "https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=600",
        "desc": "Circular Quay에서 페리 30분. 본다이보다 한적하고 서핑 문화 최고.",
        "tip": "페리 타고 가는 길의 하버 뷰가 무료 크루즈급! 꼭 갑판에 서세요.",
        "duration": "반나절~하루",
        "cost": "페리 오팔카드 적용",
        "tags": ["비치", "서핑", "페리"]
    },
    {
        "id": 8,
        "name": "Blue Mountains",
        "category": "자연/당일치기",
        "area": "시드니 외곽 (2시간)",
        "image": "https://images.unsplash.com/photo-1494233892892-84542a694e72?w=600",
        "desc": "세자매봉(Three Sisters), 유칼립투스 숲의 푸른 안개가 장관!",
        "tip": "기차로 2시간. Scenic Railway(세계에서 가장 가파른 열차) 꼭 타세요!",
        "duration": "하루 (당일치기)",
        "cost": "기차 + 입장료 $50~",
        "tags": ["자연", "당일치기", "하이킹"]
    },
    {
        "id": 9,
        "name": "Darling Harbour",
        "category": "복합문화",
        "area": "Darling Harbour",
        "image": "https://images.unsplash.com/photo-1524820197278-540916411e20?w=600",
        "desc": "SEA LIFE 수족관, 와일드라이프 동물원, 맛집, 불꽃놀이까지!",
        "tip": "토요일 밤 9시 무료 불꽃놀이! 놓치지 마세요.",
        "duration": "반나절",
        "cost": "무료 (시설 별도)",
        "tags": ["야경", "불꽃놀이", "쇼핑"]
    },
    {
        "id": 10,
        "name": "Barangaroo Reserve",
        "category": "자연/도심",
        "area": "Barangaroo",
        "image": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=600",
        "desc": "새로 개발된 워터프론트 공원. 산책하며 하버브릿지 뷰 감상.",
        "tip": "선셋 산책 후 바란가루 하우스 루프탑 바에서 한 잔 하면 완벽!",
        "duration": "1시간",
        "cost": "무료",
        "tags": ["무료", "산책", "선셋"]
    },
]

TIPS = [
    {
        "id": 1,
        "icon": "🚇",
        "title": "교통 - Opal Card 필수!",
        "content": "공항에서 바로 구매 가능. 버스, 기차, 페리, 트램 모두 사용. 일요일은 하루 $2.50 캡! 일요일에 먼 곳 몰아서 다니면 교통비 절약.",
        "category": "교통"
    },
    {
        "id": 2,
        "icon": "☀️",
        "title": "자외선 진짜 주의!",
        "content": "호주 자외선은 한국의 3-5배. SPF50+ 선크림 필수, 모자 꼭 챙기세요. 흐린 날도 자외선 강해요! 현지인들도 다 바르고 다님.",
        "category": "건강"
    },
    {
        "id": 3,
        "icon": "💰",
        "title": "팁 문화 - 안 줘도 OK",
        "content": "호주는 팁 문화가 없어요! 레스토랑에서 팁 안 줘도 전혀 이상하지 않아요. 다만 정말 좋았으면 10% 정도 줘도 좋음.",
        "category": "문화"
    },
    {
        "id": 4,
        "icon": "🏖️",
        "title": "해변 안전 수칙",
        "content": "빨간-노란 깃발 사이에서만 수영! 이건 진짜 중요해요. 이안류(rip current) 위험. 라이프가드 있는 해변에서만 수영하세요.",
        "category": "안전"
    },
    {
        "id": 5,
        "icon": "🔌",
        "title": "콘센트 어댑터",
        "content": "호주는 I타입 콘센트 (팔자형). 한국 충전기 안 맞아요! 공항 도착하자마자 사거나 한국에서 미리 구매.",
        "category": "준비물"
    },
    {
        "id": 6,
        "icon": "🛒",
        "title": "마트 꿀팁",
        "content": "Woolworths, Coles 양대 마트. 저녁 7시 이후 할인 스티커 붙은 상품 노리세요. Aldi가 가장 저렴! 물가가 비싸니 마트 적극 활용.",
        "category": "절약"
    },
    {
        "id": 7,
        "icon": "📱",
        "title": "유심/eSIM 추천",
        "content": "공항에서 Optus, Vodafone 유심 구매 가능. eSIM이면 Airalo나 Ubigi 추천. 28일 기준 $30~40 정도. 데이터 넉넉하게!",
        "category": "통신"
    },
    {
        "id": 8,
        "icon": "🕐",
        "title": "시차 & 영업시간",
        "content": "한국보다 +2시간 (서머타임 시 +2). 상점은 대부분 5-6시에 닫아요! 목요일만 Late Night Shopping(9시까지). 쇼핑은 목요일에!",
        "category": "생활"
    },
    {
        "id": 9,
        "icon": "🌊",
        "title": "무료로 즐기는 시드니",
        "content": "Bondi to Coogee 워크, 보타닉 가든, The Rocks 마켓 구경, 하버브릿지 도보, 오페라하우스 외관, Barangaroo 산책 - 다 무료!",
        "category": "절약"
    },
    {
        "id": 10,
        "icon": "🍺",
        "title": "호주 커피 & 술 문화",
        "content": "호주 커피 수준은 세계 최고급. Flat White 꼭 마셔보세요! 술은 비싼 편. BWS, Dan Murphy's에서 사서 마시는 게 절약 팁.",
        "category": "문화"
    },
    {
        "id": 11,
        "icon": "🦘",
        "title": "호주 동물 만나기",
        "content": "Taronga Zoo 말고도 Featherdale Wildlife Park에서 코알라 안고 사진 가능! Wild Life Sydney Zoo는 달링하버에 있어 접근성 좋음.",
        "category": "체험"
    },
    {
        "id": 12,
        "icon": "📸",
        "title": "인생샷 포인트 TOP 3",
        "content": "1) Mrs Macquarie's Chair - 오페라하우스+브릿지 투샷 2) Bondi Icebergs Pool - 해변+수영장 3) Milsons Point - 루나파크에서 오페라하우스 뷰",
        "category": "포토"
    },
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/restaurants')
def get_restaurants():
    return jsonify(RESTAURANTS)


@app.route('/api/attractions')
def get_attractions():
    return jsonify(ATTRACTIONS)


@app.route('/api/tips')
def get_tips():
    return jsonify(TIPS)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
