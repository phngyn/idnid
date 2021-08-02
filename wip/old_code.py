import bs4
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from pprint import pprint

write_file = "C:\\Users\\phngu\\OneDrive\\dev\\Projects\\webscrape\\rings.txt"

href_collect = []
last_page = 47
for i in range(1, last_page + 1):
    my_url = "https://www.idonowidont.com/marketplace/engagement-rings?page=" + str(i)
    # print(my_url)

    #Opens the webpage, reads it into a container, then closes the client
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()

    #Uses soup to parse down to href to get weblink
    soup_html = bs(page_html, "html.parser")
    container = soup_html.findAll("div", {"class":"ds-1col"})

    for i in range(len(container)):
        href_collect.append(container[i].div.a["href"])


# for i in href_collect:
#     print("https://www.idonowidont.com" + i)

rings = []
href_collect = ['/diamonds/engagement-ring-princess-cut-730826', '/diamonds/301-elongated-cushion-cut-gia-cert-lab-grown-730194', '/diamonds/gia-certified-271-ctw-3-stone-old-european-cut-ring-730193', '/diamonds/cushion-cut-engagement-ring-730825', '/diamonds/exquisite-diamond-edwardian-vintage-ring-size-525-730824', '/diamonds/ladies-diamond-engagement-ring-730822', '/diamonds/forevermark-5-diamond-halo-18k-white-gold-ring-730820', '/diamonds/beautiful-46-carat-brilliant-round-cut-solitaire-diamond-ring-14k-gold-size-575-730818', '/diamonds/jared-new-gorgeous-engagement-ring-730813', '/diamonds/cushion-cut-moissanite-ring-730816', '/diamonds/14k-white-gold-diamond-cluster-engagement-ring-730809', '/diamonds/18-k-diamond-halo-engagement-ring-size-5-12-vs-2-150-tcw-609521', '/diamonds/robbins-brothers-91ct-excellent-princess-cut-engagement-ring-730807', '/diamonds/ladies-circa-1970s-diamond-ring-730802', '/diamonds/rose-gold-cushion-cut-730795', '/diamonds/neil-lane-engagement-ring-band-730801', '/diamonds/kay-jewelers-princess-cut-1ct-engagement-ring-730800', '/diamonds/14kt-white-gold-diamond-bridal-set-one-round-brilliant-ideal-cut-center-diamond-12ct-730798', '/diamonds/51-carat-diamond-engagement-ring-730792', '/diamonds/disney-snow-white-bridal-set-730790', '/diamonds/brilliant-earth-ruby-14k-rose-gold-engagement-ring-730791', '/diamonds/diamonds-direct-14k-white-gold-engagement-ring-730789', '/diamonds/princess-cut-diamond-wedding-set-730787', '/diamonds/gorgeous-round-cut-diamond-730785', '/diamonds/five-diamond-wedding-band-730784', '/diamonds/robbins-brothers-cherish-wedding-set-730780', '/diamonds/marquise-solitaire-wedding-set-730776', '/diamonds/verragio-ins-7050r-30-ct-engagement-ring-730775', '/diamonds/373-carat-european-cut-engagement-ring-730773', '/diamonds/platinum-engagement-ring-730772', '/diamonds/diamond-engagement-ring-730686', '/diamonds/6-prong-125-carat-solitaire-engagement-ring-730768', '/diamonds/stunning-vintage-style-white-gold-diamond-halo-ring-diamond-set-shoulders-44k-historic', '/diamonds/ladies-diamond-engagement-ring-730764', '/diamonds/151-ct-center-stone-round-brilliant-excelent-wedding-band-2-ct-total-730763', '/diamonds/art-deco-halo-engagement-ring-730762', '/diamonds/round-brilliant-wedding-set-730761', '/diamonds/25-ct-si1-oval-halo-engagement-ring-gia-certified-730756', '/diamonds/zales-celebration-diamond-collection-engagement-ring-730753', '/diamonds/tiffany-co-princess-cut-diamond-ring-730752', '/diamonds/marquise-cut-14k-yellow-gold-diamond-ring-48ct-gemstone-50ct-side-stones-730751', '/diamonds/kay-jewelers-round-engagement-ring-730742', '/diamonds/kay-jewelers-diamond-princess-cut-engagement-ring-diamond-band-730739', '/diamonds/zales-14k-marquise-engagement-ring-730738', '/diamonds/engagement-ring-and-wedding-band-730553', '/diamonds/beautiful-18k-white-gold-19-carat-cushion-cut-diamond-wedding-set-730740', '/diamonds/rose-gold-engagment-ring-w-wedding-band-730743', '/diamonds/engagement-ring-%C3%A9tincelle-cartier-730746', '/diamonds/diamond-vault-65-solitaire-730748', '/diamonds/elegant-classy-15-carat-platinum-engagement-ring-730736', '/diamonds/deal-wont-last-123-carat-vintage-cushion-cut-diamond-white-gold-mounting-730735', '/diamonds/great-deal-171-carat-diamond-saphire-ring-white-gold-730734', '/diamonds/111-ct-princess-cut-diamond-engagement-ring-730737', '/diamonds/p%E1%B4%80s%E1%B4%9B-p%CA%80%E1%B4%87s%E1%B4%87%C9%B4%E1%B4%9B-f%E1%B4%9C%E1%B4%9B%E1%B4%9C%CA%80%E1%B4%87-p%CA%80%C9%AA%C9%B4%E1%B4%84%E1%B4%87ss-c%E1%B4%9C%E1%B4%9B-730731', '/diamonds/opal-and-diamond-engagement-set-730732', '/diamonds/valina-wedding-set-730730', '/diamonds/120-ct-radiant-gia-certified-engagement-ring-564371', '/diamonds/260ct-blue-nile-engagement-ring-730606', '/diamonds/james-allen-emerald-cut-diamond-and-platinum-engagement-ring-730725', '/diamonds/jared-14k-white-gold-engagement-ring-and-band-730724', '/diamonds/213-ct-solitaire-round-diamond-730723', '/diamonds/solitaire-round-brilliant-diamond-engagement-ring-730728', '/diamonds/vera-wang-bridal-set-730722', '/diamonds/314ct-round-brilliant-engagement-ring-fancy-pink-side-diamonds-egl-certified-incredible', '/diamonds/whitehall-jewelers-125-ct-wedding-set-730717', '/diamonds/4-quad-princess-cut-bridal-set-730721', '/diamonds/zales-engagement-ring-730720', '/diamonds/wedding-band-730718', '/diamonds/moissanite-engagement-ring-730716', '/diamonds/neil-lane-wedding-ring-and-band-730713', '/diamonds/certified-tanzanite-diamond-round-platinum-950-123ct-double-halo-engagement-ring-730714', '/diamonds/050ct-igi-certified-forever-diamond-engagement-ring-18k-white-gold-uk-hallmarked-730715', '/diamonds/tolkowsky-ideal-cut-diamond-set-platinum-engagement-ring-730712', '/diamonds/jared-730711', '/diamonds/split-pave-band-cushion-cut-engagement-ring-730709', '/diamonds/engagement-ring-730710', '/diamonds/beautiful-round-diamond-over-3-carats-730706', '/diamonds/heart-diamond-engagement-ring-730705', '/diamonds/diamonds-direct-stunning-cushion-cut-solitaire-engagement-ring-platinum-730702', '/diamonds/zales-wedding-ring-wedding-band-sale-730701', '/diamonds/custom-marquise-engagement-ring-730698', '/diamonds/princess-cut-engagement-ring-730697', '/diamonds/205-ct-solitaire-round-brilliant-diamond-ring-730696', '/diamonds/155-ct-round-brilliant-solitaire-diamond-ring-730695', '/diamonds/unique-green-diamond-engagement-ring-730693', '/diamonds/ladie%E2%80%99s-diamond-engagement-ring-730689', '/diamonds/platinum-diamond-solitaire-ring-5-carat-730688', '/diamonds/custom-made-ladies-platinum-sapphire-and-diamond-three-stone-ring-730683', '/diamonds/2-ct-diamond-solitaire-730684', '/diamonds/gold-round-centermarquise-side-diamond-ring-730678', '/diamonds/round-moissanite-pave-engagement-ring-730679', '/diamonds/princess-cut-engagement-ring-2-carats-730667', '/diamonds/85-carat-radiant-cut-ring-custom-made-730682', '/diamonds/stunning-solitaire-masterpiece-730671', '/diamonds/round-brilliant-ring-730676', '/diamonds/engagement-ring-sale-730672', '/diamonds/ladys-14kt-rose-gold-pear-shaped-engagement-ring-730669', '/diamonds/princess-cut-engagement-ring-2-carats-730666', '/diamonds/moissanite-princess-cut-diamond-2ctw-950-platinum-art-deco-engagement-ring-730664', '/diamonds/tiffany-diamond-730665', '/diamonds/helzberg-14k-engagementwedding-band-set-my-loss-your-gain-730668', '/diamonds/princess-cut-diamond-halo-top-hidden-sapphires-custom-engagement-ring-196-total-cts-730674', '/diamonds/na-hoku-diamond-engagement-ring-730675', '/diamonds/vera-wang-love-collection-1-13-ct-tw-emerald-cut-diamond-double-frame-engagement-ring-14k', '/diamonds/james-allen-067-carat-brilliant-pear-engagement-ring-14k-white-gold-730662', '/diamonds/jared-14k-platinum-engagement-ring-wedding-band-730660', '/diamonds/recycled-14k-gold-engagement-ring-floating-diamond-prong-730659', '/diamonds/tiffany-co-137-vs1-g-730656', '/diamonds/jaffe-wedding-set-sale-730655', '/diamonds/tacori-engagement-ring-730653', '/diamonds/101-diamond-ring-730652', '/diamonds/halo-diamond-engagement-ring-730650', '/diamonds/oval-halo-12-ct-center-stone-gia-certified-730649', '/diamonds/204-carat-cushion-cut-halo-730603', '/diamonds/past-present-future-ring-730646', '/diamonds/helzberg-masterpiece-wedding-set-730640', '/diamonds/black-hills-gold-wedding-set-730644', '/diamonds/hearts-eternity-bridal-set-730643', '/diamonds/zales-elegant-vintage-style-round-cut-diamond-engagement-ring-730642', '/diamonds/310-emerald-cut-diamond-ring-730635', '/diamonds/round-diamond-wedding-set-730631', '/diamonds/timeless-cushion-cut-ring-730630', '/diamonds/stunning-infinity-diamond-ring-730629', '/diamonds/beautiful-custom-designed-anniversary-ring-730627', '/diamonds/discounted-new-wedding-set-730626', '/diamonds/engagement-and-wedding-band-set-730625', '/diamonds/forever-one-moissanite-engagement-ring-730624', '/diamonds/princess-cut-14kw-3-stone-ring-116ct-tw-730623', '/diamonds/801-round-brilliant-engagement-ring-730618', '/diamonds/solitaire-engagement-ring-730622', '/diamonds/vintage-style-tacori-engagement-ring-730621', '/diamonds/round-brilliant-diamond-18k-yellow-gold-band-and-platinum-6-prong-setting-730619', '/diamonds/brilliant-earth-18k-white-gold-twilight-lab-diamond-ring-moissanite-size-65-730616', '/diamonds/125-tcw-platinum-princess-cut-engagement-ring-d-color-matching-wedding-band-730615', '/diamonds/14-karat-white-gold-diamond-engagement-ring-730614', '/diamonds/rose-gold-round-diamond-engagement-ring-730608', '/diamonds/engagement-ring-purchased-never-proposed-730605', '/diamonds/round-brilliant-cut-diamond-730604', '/diamonds/princess-shaped-wedding-ring-set-730602', '/diamonds/2-carat-eternity-band-white-gold-730601', '/diamonds/diamonds-direct-princess-cut-engagement-ring-730599', '/diamonds/halo-bridal-set-730598', '/diamonds/205-tcw-bespoke-emerald-engagement-ring-162-ctw-center-stone-w-diamond-baguette-prongs', '/diamonds/2-%C2%BD-ct-round-solitaire-diamond-engagement-ring-730591', '/diamonds/james-allen-round-diamond-engagement-ring-730588', '/diamonds/round-diamond-engagement-ring-730587', '/diamonds/tiffany-co-solitaire-diamond-ring-730585', '/diamonds/ladies-14kt-two-tone-gold-diamond-and-sapphire-ring-730584', '/diamonds/forevermark-engagement-ring-730563', '/diamonds/unique-setting-75-center-round-diamond-730581', '/diamonds/10kw%E2%80%9Drd-dia-wbl-sappi-730573', '/diamonds/round-brilliant-ring-your-dreams-730580', '/diamonds/beautiful-oval-diamond-ring-730578', '/diamonds/last-chance-round-brilliant-1-carat-diamond-engagement-ring-leo-collection-jared-730577', '/diamonds/diamond-and-sapphire-ring-fair-market-value-730568', '/diamonds/engagement-wedding-band-combo-730566', '/diamonds/white-gold-diamond-engagement-ring-730564', '/diamonds/hearts-fire-engagement-ring-and-wedding-band-730561', '/diamonds/beautiful-art-deco-style-engagement-ring-sale-730560', '/diamonds/tacori-wedding-set-730558', '/diamonds/round-cut-engagement-ring-07-ct-i1-clarity-g-color-730556', '/diamonds/blue-nile-custom-engagement-ring-high-quality-single-diamond-730555', '/diamonds/custom-made-90ct-cushion-cut-diamond-ring-730552', '/diamonds/zales-engagement-ring-band-730551', '/diamonds/forevermark-briliant-white-gold-engagement-ring-520976', '/diamonds/solitaire-engagement-ring-730549', '/diamonds/072-carat-princess-cut-engagement-ring-543191', '/diamonds/verragio-venetian-collection-full-set-all-excellent-condition-includes-side-stone-semi', '/diamonds/258-carat-diamond-solitaire-730538', '/diamonds/tiffany-solitaire-ring-730534', '/diamonds/jareds-engagement-ring-wrapping-bands-730533', '/diamonds/kay-jewelers-14k-diamond-ring-and-band-730532', '/diamonds/jared-new-14k-white-gold-90-carat-diamond-engagement-ring-matching-wedding-band-730530', '/diamonds/jared-pear-shape-diamond-14k-yellow-gold-wedding-rings-730527', '/diamonds/2ctw-split-shank-halo-engagement-ring-baguette-wedding-band-728295', '/diamonds/205-ct-lab-grown-round-brilliant-diamond-ring-730529', '/diamonds/197-carat-center-stone-271-carat-total-tiffany-co-platinum-and-diamond-engagement-ring', '/diamonds/timeless-282-tcw-radiant-cut-diamond-ring-730521', '/diamonds/engagement-ring-and-wedding-band-730520', '/diamonds/18-total-carat-rose-gold-oval-diamond-engagement-ring-730518', '/diamonds/ladies-151-carat-yellow-gold-six-prong-solitaire-engagement-ring-730516', '/diamonds/lab-grown-155-ct-round-brilliant-diamond-engagement-ring-730517', '/diamonds/wedding-and-engagement-bands-730514', '/diamonds/104ct-natural-ruby-and-diamond-halo-ring-platinum-orianne-collins-730512', '/diamonds/kay-jewelers-bridal-set-730511', '/diamonds/rare-and-different-287-carat-diamond-ring-cushion-cut-diamond-deal-day-730509', '/diamonds/great-deal-511-carat-diamond-ring-princess-cut-platinum-setting-style-730508', '/diamonds/lab-grown-251ct-round-brilliant-diamond-ring-730515', '/diamonds/diamond-and-aquamarine-engagement-ring-730506', '/diamonds/verragio-exquisite-engagement-ring-2-woman%E2%80%99s-wedding-bands-and-men%E2%80%99s-wedding-band-730503', '/diamonds/pear-shaped-engagement-ring-730498', '/diamonds/princess-cut-diamond-engagement-ring-730501', '/diamonds/diamond-ring-appraised-3k-730485', '/diamonds/simond-g-halo-diamond-ring-730484', '/diamonds/kay-jewelers-women%E2%80%99s-2-tone-1-ct-bridal-set-730479', '/diamonds/rose-gold-anniversary-or-engagement-ring-730472', '/diamonds/2ct8mm-round-moissanite-petite-cushion-halo-engagement-ring-730478', '/diamonds/brilliant-round-solitaire-diamond-engagement-ring-yellow-gold-band-730473', '/diamonds/marquise-cut-beautiful-ring-730441', '/diamonds/three-stone-diamond-engagement-ring-730439', '/diamonds/forevermark-halo-diamond-engagement-ringprice-dropped-730003', '/diamonds/jared-jewelers-round-brilliant-classic-engagement-ring-730431', '/diamonds/zales-wedding-ring-set-730430', '/diamonds/65-carat-platinum-cushion-cut-moon-sides-engagement-ring-730419', '/diamonds/brilliant-earth-solitaire-moissanite-engagement-ring-730415', '/diamonds/kay-jewelers-engagement-set-730413', '/diamonds/custom-design-princess-cut-size-675-730409', '/diamonds/061ct-igi-certified-h-vs1-platinum-princess-engagement-ring-730407', '/diamonds/white-gold-halo-style-princess-cut-wedding-set-730396', '/diamonds/custom-crafted-engagement-ring-featuring-prong-set-round-moissanite-center-stone-flanked', '/diamonds/lab-grown-emerald-cut-engagement-ring-730400', '/diamonds/tacori-dantela-2-carat-730333', '/diamonds/halo-engagement-ring-730379', '/diamonds/natalie-k-diamond-ring-200-carat-total-730380', '/diamonds/gia-certified-e-color-3-stone-princess-cut-engagement-ring-wedding-band-730375', '/diamonds/066ct-round-diamond-halo-engagement-ring-wedding-ring-bridal-set-18k-white-gold-730361', '/diamonds/45-asscher-cut-sides-diamond-ring-730359', '/diamonds/leo-cut-diamond-wedding-set-730356', '/diamonds/new-486-carat-pear-cut-3-stone-diamond-ring-730345', '/diamonds/helzberg%E2%80%99s-gorgeous-round-brillant-wedding-ring-730334', '/diamonds/sholdt-design-solitaire-engagement-ring-size-7-091-carat-730326', '/diamonds/215-ct-vs2-round-solitaire-engagement-ring-730309', '/diamonds/4-carat-diamond-ring-35-radiant-cut-center-730311', '/diamonds/318-carat-wedding-set-218-ivs2-triple-excellent-730317', '/diamonds/57-carat-oval-stunner-730312', '/diamonds/vera-wang-love-diamond-ring-730298', '/diamonds/141-total-ct-diamond-engagementwedding-ring-set-appraised-4250-15-years-ago-730290', '/diamonds/140-ctw-round-brilliant-diamond-engagement-ring-730297', '/diamonds/83-antique-style-engagement-ring-730279', '/diamonds/custom-claddagh-ring-730270', '/diamonds/kay-jewelers-diamond-solitaire-engagement-ring-1-ct-tw-princess-cut-10k-white-gold-730271', '/diamonds/round-brilliant-diamond-ring-wedding-set-730276', '/diamonds/267ct-round-brilliant-lab-grown-diamond-ring-730275', '/diamonds/80ct-princess-cut-diamond-halo-ring-730273', '/diamonds/zales-14k-white-gold-quad-princess-cut-engagement-ring-730253', '/diamonds/zales-love%E2%80%99s-destiny-engagement-ring-730252', '/diamonds/helzberg-limited-edition-style-engagement-ring-princess-cut-white-gold-730239', '/diamonds/engagement-setting-not-including-center-diamond-730237', '/diamonds/1-ct-spiral-halo-vera-wang-love-collection-sapphire-mounting-730234', '/diamonds/12-ct-antique-style-diamond-engagement-wedding-ring-set-sapphires-14k-white-gold-designer', '/diamonds/gia-certified-058ct-d-vvs1-xxx-diamond-platinum-solitaire-engagement-ring-730224', '/diamonds/317ct-igi-certified-emerald-diamond-ring-platinum-18k-gold-new-730225', '/diamonds/new-254ct-hrd-certified-vvs1-diamond-tiffany-co-style-platinum-solitaire-engagement-ring', '/diamonds/new-101ct-igi-certified-vs1-emerald-diamond-tiffany-style-platinum-solitaire-engagement', '/diamonds/103ct-gia-certified-platinum-princess-diamond-halo-engagement-ring-halo-730228', '/diamonds/050ct-gia-igi-certified-platinum-round-diamond-solitaire-engagement-ring-730229', '/diamonds/050ct-gia-certified-f-si1-xxx-excellent-cut-diamond-platinum-halo-engagement-ring-730230', '/diamonds/certified-071ct-h-si1-diamond-platinum-solitaire-engagement-ring-730231', '/diamonds/025ct-pear-cut-diamond-solitaire-engagement-ring-14k-yellow-gold-730214', '/diamonds/305-traditional-tiffany-style-diamond-ring-yellow-gold-plat-head-igi-cerified-ring-730218', '/diamonds/97ct-princess-cut-diamond-engagement-ring-wedding-band-set-730205', '/diamonds/gorgeous-neil-lane-wedding-set-730182', '/diamonds/platinum-033ct-certified-princess-diamond-solitaire-engagement-ring-730178', '/diamonds/116tcw-rachael-engagement-ring-ken-and-dana-design-730167', '/diamonds/543-carat-diamond-ring-730166', '/diamonds/leo-princess-cut-w-sapphire-stones-engagement-ring-730154', '/diamonds/343-carat-diamond-ring-amazing-ring-see-video-730157', '/diamonds/233-tacori-engagement-ring-177-g-vs1-center-730145', '/diamonds/07-carat-engagement-ring-two-bands-730136', '/diamonds/460-yellow-gold-cushion-solitaire-730114', '/diamonds/diamond-three-stone-engagement-ring-toby-rhinehart-design-730090', '/diamonds/zei-engagement-ring-730019', '/diamonds/two-row-139-tcw-round-diamond-wedding-ring-730077', '/diamonds/99-ct-princess-cut-engagement-ring-730076', '/diamonds/120-ctw-three-stone-diamond-ring-730075', '/diamonds/beautiful-princess-cut-diamond-engagement-wedding-ring-730072', '/diamonds/beautiful-engagement-wedding-ring-set-730074', '/diamonds/diamond-engagement-ring-marquise-cut-yellow-and-white-gold-matching-diamond-ring-guard', '/diamonds/diamond-wedding-ring-730026', '/diamonds/stunning-161-ct-194-tcw-brilliant-earth-engagement-ring-730006', '/diamonds/202-ct-cushion-benz-14k-white-gold-setting-w-5ct-band-730001', '/diamonds/gorgeous-round-cut-151-ct-engagement-ring-729985', '/diamonds/2-carat-total-weight-diamond-band-or-anniversary-ring-729983', '/diamonds/round-bypass-channel-moissanite-engagement-ring-729970', '/diamonds/new-loose-pink-diamond-151-carats-video-link-igi-certified-rose-gold-ring-729933', '/diamonds/michael-m-wedding-rings-set-729932', '/diamonds/tiffany-co-lucida-diamond-platinum-ring-729929', '/diamonds/249ct-egl-certified-g-vs2-platinum-bridal-set-bespoke-729900', '/diamonds/140ct-gia-certified-cushion-halo-engagement-ring-18k-white-gold-729913', '/diamonds/176ct-igi-certified-marquise-halo-14k-white-gold-engagement-ring-729909', '/diamonds/120ct-gia-round-halo-engagement-ring-18k-white-gold-james-allen-729911', '/diamonds/video-gia-certified-200ct-tiffany-co-style-round-k-vs2-excellent-cut-diamond-18k-yellow', '/diamonds/130ct-egl-usa-certified-round-diamond-engagement-ring-14k-white-gold-729912', '/diamonds/102ct-agsl-certified-i-si2-round-solitaire-14k-white-gold-engagement-ring-729902', '/diamonds/125ct-gia-certified-f-vvs2-round-accent-engagement-ring-18k-white-gold-729905', '/diamonds/157ct-certified-princess-diamond-platinum-engagement-ring-729906', '/diamonds/tacori-bridal-set-platinum-engagement-ring-wedding-ring-729907', '/diamonds/169ct-egl-usa-certified-cushion-halo-engagement-ring-14k-white-gold-729910', '/diamonds/143ct-gia-certified-f-vvs1-princess-trilogy-engagement-ring-platinum-729908', '/diamonds/video-new-gia-certified-tiffany-co-style-101ct-f-vs1-xxx-diamond-platinum-solitaire', '/diamonds/141ct-gia-certified-e-si2-platinum-princess-trilogy-ring-729901', '/diamonds/video-gia-certified-tiffany-co-style-100ct-d-vs2-diamond-platinum-solitaire-engagement-ring', '/diamonds/classic-vintage-diamond-bypass-ring-729879', '/diamonds/tacori-engagement-ring-729871', '/diamonds/video-tiffany-and-co-platinum-075ct-diamond-lucida-cut-radiant-square-princess-asscher', '/diamonds/jared-engagement-ring-3-carat-729838', '/diamonds/500-ct-moisanite-diamond-ring-729827', '/diamonds/asscher-cut-diamond-ring-25-i-vs1-gia-729833', '/diamonds/1-ctw-double-halo-diamond-engagement-ring-wedding-band-set-10k-white-gold-725396', '/diamonds/15-carat-diamond-round-cut-double-halo-engagement-ring-set-10k-white-gold-728659', '/diamonds/diamonds-direct-14-karat-white-gold-3-stone-engagement-ring-729804', '/diamonds/630-ct-radiant-diamond-729798', '/diamonds/1ct-tacori-halo-diamond-engagement-ring-and-band-729771', '/diamonds/engagement-ring-10-ct-729756', '/diamonds/fancy-yellow-diamond-ring-729736', '/diamonds/diamond-ring-729735', '/diamonds/tanzanite-heart-and-diamond-ring-729734', '/diamonds/citrine-and-diamond-ring-729733', '/diamonds/636-carat-round-diamond-ring-729739', '/diamonds/gia-certified-85-radiant-14k-gold-custom-bridal-ring-set-729730', '/diamonds/tiffany-cushion-cut-101-ct-white-14-karat-engagement-ring-18-karat-full-anniversary', '/diamonds/313-carat-diamond-engagement-ring-263-j-si1-ex-ex-ex-center-729699', '/diamonds/jared-cushion-cut-diamond-engagement-ring-729697', '/diamonds/jared-116-05-ct-princess-cut-solitaire-engagement-ring-729670', '/diamonds/diamonds-direct-251c-gia-certified-princess-cut-solitaire-engagement-ring-679471', '/diamonds/james-allen-3-ct-oval-lab-grown-diamond-engagement-ring-729679', '/diamonds/109ct-engagement-ring-14k-white-gold-simple-setting-thin-band-size-7-729644', '/diamonds/461-carat-cushion-solitaire-729639', '/diamonds/14-kt-white-gold-halo-style-engagement-ring-729638', '/diamonds/classic-five-stone-engagement-ring-features-185ct-total-diamonds-620861', '/diamonds/impressive-gia-certified-engagement-ring-center-076ct-pear-shape-fancy-yellow-diamond', '/diamonds/verragio-insignia-engagement-ring-wedding-band-729589', '/diamonds/huge-bling-statement-ring-hand-made-nyc-638716', '/diamonds/gia-certified-engagement-ring-611-carat-yellow-cushion-cut-diamond-659791', '/diamonds/267-carat-fancy-yellow-radiant-cut-diamond-engagement-ring-platinum-659786', '/diamonds/custom-moissanite-platinum-engagement-ring-729529', '/diamonds/egl-usa-certified-222ct-fancy-yellow-18k-white-gold-diamond-halo-engagement-ring-brand-new', '/diamonds/2-ctw-double-halo-diamond-engagement-ring-wedding-band-set-10k-white-gold-725401', '/diamonds/385ct-natural-vvs-indocilite-bi-color-blue-tourmaline-722971', '/diamonds/tiffany-style-legacy-aquamarinediamond-ring-729433', '/diamonds/pear-shape-diamond-ring-342-carat-18kt-white-gold-certified-729408', '/diamonds/346-ct-pear-diamond-ring-729406', '/diamonds/jared-princess-engagementwedding-set-729404', '/diamonds/14k-gold-black-and-white-diamond-ring-729402', '/diamonds/round-diamond-807-carat-great-deal-729348', '/diamonds/wow-pear-shape-diamond-681-carat-certified-729347', '/diamonds/great-deal-round-custom-made-diamond-ring-305-carat-hand-crafted-18kt-white-gold-729341', '/diamonds/beautiful-diamond-ring-171-carat-diamond-ring-deal-wont-last-729343', '/diamonds/rare-and-different-177-carat-diamond-ring-cushion-cut-diamond-729342', '/diamonds/253-cushion-solitaire-diamond-ring-729335', '/diamonds/custom-carved-wrap-style-engagement-ring-729334', '/diamonds/1ct-fancy-deep-yellowish-brown-engagement-ring-729313', '/diamonds/149-ct-round-diamond-ring-729261', '/diamonds/platinum-sapphire-and-diamond-engagement-ring-729254', '/diamonds/611-carat-platinum-halo-cushion-diamond-engagement-ring-729228', '/diamonds/jb-star-design-halo-engagement-ring-729201', '/diamonds/wow-deal-wont-last-631-carat-diamond-ring-certified-all-custom-made-729175', '/diamonds/gabriel-co-gorgeous-131-carat-marquise-diamond-engagement-ring-729186', '/diamonds/65-carat-wedding-set-matching-band-729154', '/diamonds/theo-fennell-540ct-asscher-cut-diamond-engagement-ring-18k-white-gold-727066', '/diamonds/neil-lane-engagement-ring-729133', '/diamonds/stunning-new-182ct-certified-diamond-engagement-ring-matching-wedding-band-729106', '/diamonds/144-ct-diamond-ring-18k-white-gold-729083', '/diamonds/35-assscher-cut-platinum-pave-diamond-engagement-ring-728937', '/diamonds/ritani-3-band-halo-ring-2-carat-ivs1-gia-center-728942', '/diamonds/170-oval-halo-diamond-ring-728929', '/diamonds/455-diamond-set-305-i-vs1-center-728926', '/diamonds/brand-new-650-carat-wedding-set-eternity-band-728925', '/diamonds/stunning-round-diamond-engagement-ring-2018-728867', '/diamonds/white-gold-wedding-set-tons-sparkle-728869', '/diamonds/engagement-ring-diamond-wedding-band-jacket-728716', '/diamonds/engagement-ring-71-vs2-f-gia-728814', '/diamonds/230-ct-gia-certified-center-diamond-pear-shape-g-color-vvs1-clarity-excellent-cut-polish', '/diamonds/diamond-cluster-halo-ring-717481', '/diamonds/10k-gold-diamond-engagement-ring-717476', '/diamonds/brilliant-earth-stunning-breathtaking-eco-friendly-diamond-ring-728768', '/diamonds/15-diamond-yellow-gold-728681', '/diamonds/three-piece-engagement-ring-and-wedding-bands-728634', '/diamonds/521-carat-platinum-custom-made-728630', '/diamonds/reeds-jewelers-kleinfeld-alwyn-engagement-ring-728569', '/diamonds/201-carat-round-excellentideal-cut-e-colorless-vvs2-clarity-6-prong-tiffany-style-14k-white', '/diamonds/220-carat-diamond-solitaire-ring-180-carat-center-728257', '/diamonds/045ct-gia-certified-d-si1-excellent-cut-halo-diamond-engagement-ring-18k-gold-728240', '/diamonds/185ctw-round-engagement-ring-727936', '/diamonds/175ctw-pear-halo-diamond-engagement-ring-727921', '/diamonds/125ctw-diamond-oval-engagement-ring-727916', '/diamonds/162-ctw-round-engagement-ring-727911', '/diamonds/150ctw-round-twisted-diamond-engagement-ring-727906', '/diamonds/150-ctw-halo-round-engagement-ring-727901', '/diamonds/150-ctw-round-halo-diamond-ring-727891', '/diamonds/14k-white-gold-engagement-ring-727861', '/diamonds/52-vs2-marquise-72ctw-g-color-engagement-ring-727851', '/diamonds/150-ctw-round-diamond-halo-engagement-ring-727796', '/diamonds/130-ctw-diamond-engagement-ring-727786', '/diamonds/112-ctw-diamond-engagement-ring-727771', '/diamonds/1ct-diamond-engagement-ring-727756', '/diamonds/130-ctw-halo-diamond-engagement-ring-727661', '/diamonds/125-ctw-diamond-engagement-ring-727656', '/diamonds/120-ctw-halo-engagement-ring-727651', '/diamonds/1-15-ctw-halo-diamond-engagment-ring-727646', '/diamonds/lab-grown-34-cttw-diamond-engagement-ring-727641', '/diamonds/canadian-maple-leaf-diamonds-e-vs2-halo-platinum-engagement-ring-727541', '/diamonds/220ct-gia-certified-platinum-cushion-diamond-halo-engagement-ring-727391', '/diamonds/140ct-certified-e-vvs1-marquise-platinum-bridal-engagement-ring-727386', '/diamonds/gia-certified-216ct-fancy-yellow-diamond-platinum-bridal-set-727376', '/diamonds/custom-14k-white-gold-diamond-and-moissanite-engagement-ring-set-wedding-bands-726866', '/diamonds/igi-certified-22k-yellow-gold-145ct-deep-blue-sapphire-and-diamond-halo-cluster-dress-ring', '/diamonds/engagementwedding-ring-726331', '/diamonds/2-ct-certified-oval-moissanite-oval-solitaire-engagement-ring-14k-yellow-gold-726061', '/diamonds/112ct-gia-certified-f-vvs2-cushion-cut-diamond-engagement-ring-14k-white-gold-725846', '/diamonds/089ct-gia-certified-e-vvs1-blue-nile-petite-twist-princess-diamond-engagement-ring-14k', '/diamonds/unique-round-brilliant-diamond-ring-set-14kt-white-gold-725811', '/diamonds/060-ct-round-brilliant-diamond-engagement-ring-725806', '/diamonds/145-ctw-emerald-cut-diamond-engagement-ring-725801', '/diamonds/brilliant-cut-solitaire-engagement-ring-wedding-band-725706', '/diamonds/kay-jewelers-diamond-engagement-ring-wenhancer-band-725691', '/diamonds/081ct-gia-certified-fancy-orange-diamond-ring-white-gold-mens-gents-unisex-725411', '/diamonds/081ct-gia-certified-scott-kay-round-diamond-solitaire-engagement-ring-724771', '/diamonds/gia-certified-094-g-si2-oval-cut-diamond-halo-engagement-ring-18k-white-gold-brilliant', '/diamonds/gia-certified-princess-cut-diamond-halo-engagement-ring-14k-gold-diamonds-direct-724761', '/diamonds/gia-certified-148ct-princess-cut-diamond-accent-engagement-ring-18k-gold-724751', '/diamonds/gia-certified-075ct-e-vs1-princess-cut-diamond-engagement-ring-14k-white-gold-724766', '/diamonds/tiffany-co-certified-118ct-classic-round-diamond-accent-engagement-ring-platinum-724776', '/diamonds/gia-certified-071ct-princess-cut-diamond-engagement-ring-14k-gold-724756', '/diamonds/igi-certified-g-vs1-163ct-round-diamond-accent-engagement-ring-wedding-ring-bridal-set-18k', '/diamonds/ags-certified-128ct-platinum-halo-round-diamond-engagement-ring-ben-bridge-724796', '/diamonds/gia-certified-209ct-round-diamond-14k-yellow-gold-solitaire-engagement-ring-wedding-ring', '/diamonds/gia-certified-128ct-princess-cut-diamond-accent-engagement-ring-14k-gold-diamonds-direct', '/diamonds/gia-certified-098ct-diamond-engagement-ring-14k-yellow-gold-724786', '/diamonds/056ct-igi-certified-emerald-cut-diamond-engagement-ring-18k-white-gold-rox-724846', '/diamonds/234ct-natural-tanzanite-and-diamond-platinum-950-bespoke-statement-dress-ring-724506', '/diamonds/corona-situation-classic-diamond-ring-162-carat-certified-split-shank-setting-style-724446', '/diamonds/video-igi-certified-d-vs2-18k-white-gold-oval-diamond-halo-engagement-ring-723721', '/diamonds/95-ctw-75-center-si-round-brilliant-723551', '/diamonds/emerald-cut-diamond-ring-723081', '/diamonds/14-kw-14-ct-echo-round-solitaire-brilliant-cut-diamond-engagement-ring-722406', '/diamonds/tourneau-de-beers-18k-gold-5-ct-solitaire-vs1-diamond-engagement-ring-722271', '/diamonds/222-carat-2-piece-ring-set-122-f-vvs2-ex-ex-ex-diamond-center-722251', '/diamonds/princess-cut-engagement-ring-wedding-band-set-size-7-722186', '/diamonds/beverly-k-design-18k-wg-halo-style-diamond-ring-size-6-round-brilliant-cut-center-diamond', '/diamonds/solitaire-princess-cut-kay-jewelers-721786', '/diamonds/200-oval-pave-diamond-ring-719381', '/diamonds/145-carat-lab-diamond-engagement-ring-14k-yellow-gold-band-721556', '/diamonds/video-025ct-hearts-fire-ags-certified-platinum-engagement-diamond-ring-721216', '/diamonds/engagement-ring-3-stunning-diamonds-coronet-setting-18-carat-gold-main-diamond-497-mm-g-si1', '/diamonds/290-emerald-cut-platinum-ring-720501', '/diamonds/great-deal-corona-situation-157-carat-diamond-ring-custom-made-certified-gemologist-720466', '/diamonds/lauren-b-radiant-halo-engagement-ring-14kt-white-gold-moissanite-diamond-halo-sz-5-720391', '/diamonds/video-110ct-natural-blue-sapphire-marquise-diamond-halo-18k-engagement-ring-720146', '/diamonds/james-allen-ladies-14k-white-gold-halo-diamond-engagement-ring-720042', '/diamonds/beautiful-sparkling-princess-cut-diamond-wedding-set-689096', '/diamonds/video-igi-certified-%E2%80%9Cleo-diamond%E2%80%9D-18k-white-gold-051ct-diamond-solitaire-round-brilliant', '/diamonds/video-gia-certified-092ct-solitaire-platinum-950-f-si1-square-princess-cut-diamond', '/diamonds/video-tacori-style-18k-white-gold-020ct-diamond-round-brilliant-vintage-accent-engagement', '/diamonds/elegant-engagement-ring-719881', '/diamonds/diamond-and-sapphire-engagement-ring-open-offers-719671', '/diamonds/cushion-halo-engagement-ring-set-sylvie-719666', '/diamonds/200-carat-double-halo-oval-diamond-ring-ivs1-gia-719616', '/diamonds/14k-white-gold-engagement-ring-and-wedding-band-set-719441', '/diamonds/vera-wang-love-collection-1-ct-tw-oval-diamond-three-stone-engagement-ring-14k-two-tone', '/diamonds/video-igi-certified-white-gold-110ct-diamond-solitaire-accent-engagement-ring-round', '/diamonds/200-carat-halo-oval-diamond-ring-ivs2-gia-719191', '/diamonds/kay-jewelers-halo-princess-cut-engagement-ring-718996', '/diamonds/blue-nile-princess-cut-wedding-set-718991', '/diamonds/155-h-vvs2-gia-cushion-twist-band-ring-718821', '/diamonds/princess-cut-109-blue-topaz-and-green-emeralds-715236', '/diamonds/399-cushion-cut-pave-ring-gia-309-i-vvs1-cushion-center-718281', '/diamonds/engagement-ring-18k-white-gold-diamond-sapphiressize-4-size-h5-video-available-instagram', '/diamonds/551-wedding-set-401-i-vs1-center-cushion-717041', '/diamonds/beautiful-matching-bridal-set-716581', '/diamonds/wow-gorgeous-cushion-halo-ring-10x10mm-moissanite-center-716251', '/diamonds/359-carat-set-gia-3-ct-i-vvs1-cushion-plus-band-716191', '/diamonds/brand-new-105mm-old-mine-cut-center-platinum-ring-side-baguettes-716041', '/diamonds/520-old-mine-cut-platinum-engagement-ring-new-715986', '/diamonds/266-ct-engagement-ring-diamonds-band-715746', '/diamonds/3-ring-set-105-mm-4-carat-old-mine-cut-moissanite-center-715561', '/diamonds/showstopper-magnificent-387-carat-diamond-and-platinum-vintage-engagement-ring-one-kind', '/diamonds/blue-nile-engagement-ring-14k-white-gold-10-carat-total-diamond-weight-center-highly-graded', '/diamonds/300-carat-diamond-engagement-ring-250-h-vs2-igi-center-714706', '/diamonds/video-new-gia-certified-platinum-134ct-diamond-halo-engagement-ring-631536', '/diamonds/182-white-gold-double-halo-122-carat-f-vvs2-round-igi-diamond-center-714506', '/diamonds/brand-new-270-halo-engagement-ring-2-ct-i-vs1-gia-center-gorgeous-714486', '/diamonds/250-oval-diamond-ring-set-ring-set-150-i-vs1-gia-oval-center-wedding-band-714386', '/diamonds/553-platinum-solitaire-diamond-ring-503-vs1-triple-excellent-gia-center-713206', '/diamonds/910-carat-natural-princess-cut-diamond-engagement-ring-wedding-ring-set-10k-white-gold', '/diamonds/12-tcw-wedding-band-10k-white-gold-713216', '/diamonds/177-simon-g-halo-diamond-ring-122-f-vvs2-ex-cut-center-713116', '/diamonds/1698000-appraised-2014-106-carat-round-classic-minimalistic-solitaire-mounted-platinum', '/diamonds/custom-made-diamondplatinum-ring-5-carat-center-712851', '/diamonds/150-h-vvs2-diamond-solitaire-cushion-h-vvs2-712881', '/diamonds/princess-cut-engagement-ring-712321', '/diamonds/303-carat-3-ring-set-gorgeous-gia-certified-711651', '/diamonds/three-ring-set-409-total-carat-weight-309-i-vvs1-gia-center-711636', '/diamonds/custom-made-halo-style-2-carat-gia-certified-center-711541', '/diamonds/12-carat-round-cut-natural-diamond-engagement-rings-women-band-10kw-solid-gold-711496', '/diamonds/2-ct-certified-moissanite-round-solitaire-engagement-ring-14k-yellow-gold-711491', '/diamonds/tacori-blue-sapphire-engagement-ring-711451', '/diamonds/389-ct-gia-cushion-cut-3-sided-pave-diamond-ring-309-i-vvs1-gia-center-698881', '/diamonds/diamond-wedding-band-711061', '/diamonds/320-carat-rose-or-white-gold-oval-ring-711031', '/diamonds/180-double-halo-style-platinum-ring-h-vvs2-cushiion-center-711011', '/diamonds/ritani-diamond-ring-2-ct-gia-certified-i-vs1-round-center-711006', '/diamonds/253-halo-cushion-diamond-ring-gia-center-710961', '/diamonds/703-triple-excellent-gia-certified-diamond-tiffany-solitaire-set-710836', '/diamonds/475-emerald-cut-diamond-eternity-band-710591', '/diamonds/330-split-shank-halo-ring-280-carat-ivs2-gia-triple-excellent-center-710301', '/diamonds/459-carat-cushion-cut-diamond-ring-3-ct-gia-i-vvs1-center-and-band-710306', '/diamonds/video-100ct-gia-certified-platinum-f-vs2-diamond-engagement-ring-bezel-set-halo-bespoke', '/diamonds/video-gia-certified-082ct-fancy-light-yellow-platinum-diamond-halo-engagement-ring-710066', '/diamonds/300-emerald-cut-gia-ring-split-shank-709606', '/diamonds/great-deal-radiant-cut-diamond-133-carat-white-gold-setting-style-709446', '/diamonds/wow-great-deal-233-carat-diamond-ring-rare-and-different-709391', '/diamonds/classic-and-beautiful-round-diamond-104-carat-certified-platinum-custom-made-709386', '/diamonds/15-carat-princess-cut-engagement-ring-pav%C3%A9-set-diamond-band-709201', '/diamonds/jacob-co-diamond-ring-171-carat-white-gold-deal-wont-last-709062', '/diamonds/14k-yellow-gold-blossoming-vine-engagement-ring-size-4-cushion-gia-084-crt-709011', '/diamonds/james-allen-075ct-oval-cut-diamond-engagement-ring-708276', '/diamonds/14k-white-gold-2-ct-center-moissanite-and-1-ct-side-natural-diamonds-side-vintage', '/diamonds/brand-new-111ctw-round-brilliant-cut-diamond-14k-white-gold-setting-706841', '/diamonds/55-carat-round-moissanite-diamond-platinum-solitaire-706776', '/diamonds/tacori-platinum-solitaire-engagement-ring-w-1178-ct-ideal-cut-brian-gavin-diamond-matching', '/diamonds/252-twist-halo-diamond-engagement-ring-2ct-ivs1gia-center-705421', '/diamonds/753-carat-platinum-diamond-ring-set-5-carat-gia-center-vs1-triple-excellent-705251', '/diamonds/253-carat-halo-203ct-gia-cushion-cut-center-704951', '/diamonds/vintage-filigree-flower-ring-704351', '/diamonds/new-250-ajaffe-new-platinum-set-w-band-150-i-vs2-radiant-gia-center-704316', '/diamonds/jared-solitaire-round-diamond-engagement-ring-703711', '/diamonds/230-ct-ring-pave-200-i-vs1-diamond-gia-certified-703166', '/diamonds/elegant-diamond-ringvideo-702901', '/diamonds/absolutely-amazing-engagement-setvideo-702896', '/diamonds/pear-shaped-diamond-white-gold-engagementband-set-702776', '/diamonds/certified-natural-cushion-engagement-ring-702291', '/diamonds/151-carat-diamond-ring-classic-and-different-18kt-white-gold-701981', '/diamonds/jaffe-180-carat-brand-new-ajaffe-engagement-ring-15-gia-center-701666', '/diamonds/deal-day-126-carat-diamond-ring-custom-made-18kt-white-gold-my-loss-your-gain-701531', '/diamonds/182-tiffany-style-solitaire-ring-701416', '/diamonds/550-platinum-custom-solitaire-moissanite-ring-11mm-old-mine-cut-gorgeous-free-wrap-701311', '/diamonds/halo-asscher-cut-diamond-ring-gia-certified-700706', '/diamonds/gorgeous-pear-wedding-set-5-cts-700346', '/diamonds/080-ctw-round-diamond-engagement-ring-699996', '/diamonds/240-ct-i-vs2-gia-center-platinum-ring-and-band-jeff-cooper-699271', '/diamonds/round-brilliant-diamond-solitaire-058-diamond-698511', '/diamonds/leo-diamond-solitaire-e-color-round-58-carat-brilliant-698506', '/diamonds/140-ct-heart-shaped-diamond-ring-698241', '/diamonds/313-diamond-engagement-ring-263-j-si1-ex-ex-ex-center-698096', '/diamonds/certified-natural-oval-engagement-ringvideo-697691', '/diamonds/unbelievable-three-stone-engagement-ringvideo-697696', '/diamonds/fantastic-engagement-ring-center-princess-cut-diamondvideo-697701', '/diamonds/agi-certified-three-stone-diamond-ring-334tdwvideo-697706', '/diamonds/gia-certified-three-stone-diamond-ringvideo-697671', '/diamonds/rare-setting-very-different-161-carat-diamond-ring-pear-shape-deal-697366', '/diamonds/deal-day-112-carat-diamond-classic-and-plain-setting-style-697391', '/diamonds/4-carat-moissanite-cushion-diamond-solitaire-692791', '/diamonds/new-ring-jeff-cooper-platinum-set-15-emerald-gia-center-696126', '/diamonds/310-oval-diamond-ring-250-center-gia-certified-695646', '/diamonds/274-ctw-pear-shaped-engagement-ring-694241', '/diamonds/100-carat-ctw-princess-cut-diamond-engagement-rings-set-694176', '/diamonds/tiffany-co-round-diamond-engagement-ring-693001', '/diamonds/amazing-natural-engagement-ringvideo-691546', '/diamonds/elegant-engagement-ringvideo-691226', '/diamonds/absolutely-amazing-engagement-ringvideo-691086', '/diamonds/200-ct-halo-oval-solitaire-gia-certified-ring-691016', '/diamonds/172-new-art-carved-ring-two-tone-rose-gold-center-row-122-f-vvs2-center-691011', '/diamonds/25-ct-square-radiant-diamond-ring-radiant-center-new-690891', '/diamonds/amazing-diamond-engagement-ringvideo-690831', '/diamonds/150-oval-double-halo-ring-gia-certified-689746', '/diamonds/beautiful-huge-engagement-ring-video-689531', '/diamonds/absolutely-gorgeous-engagement-ringvideo-689451', '/diamonds/108-carat-emerald-cut-solitaire-688486', '/diamonds/new-fantastic-engagement-ringvideo-688126', '/diamonds/white-gold-round-diamond-engagement-ring-and-wedding-band-688051', '/diamonds/rose-gold-engagement-ringvideo-687886', '/diamonds/very-interesting-engagement-ring-video-687836', '/diamonds/absolutely-gorgeous-engagement-ringvideo-687771', '/diamonds/new-new-new-engagement-ringvideo-687766', '/diamonds/400-carat-eternity-band-687116', '/diamonds/beautiful-princess-cut-engagement-ring-686612', '/diamonds/170-oval-ivs2-color-gia-certified-center-yellow-twist-rope-band-design-686196', '/diamonds/gabriel-co-14kt-rose-gold-and-round-diamond-designer-engagement-ring-686101', '/diamonds/kwiat-cushion-diamond-engagement-ring-pave-basket-and-band-platinum-685686', '/diamonds/new-certificated-princess-cut-3-stone-diamond-engagement-ring-685211', '/diamonds/engagement-ring-240-ct-total-diamond-weight-685236', '/diamonds/breathtaking-diamond-ring-agi-certificate-684866', '/diamonds/extraordinary-engagement-ring-center-116ct-princess-cut-diamond-video-684876', '/diamonds/three-stone-engagement-ring-684886', '/diamonds/gorgeous-engagement-ring-256-ct-total-diamond-weight-video-684891', '/diamonds/230-cushion-diamond-ring-gia-certifiednew-684931', '/diamonds/fantastic-gia-certified-engagement-ring-684731', '/diamonds/tiffany-style-cushion-cut-diamond-ring-684726', '/diamonds/agi-certified-round-diamond-engagement-ring-226-ct-total-diamond-weight-684721', '/diamonds/amazing-natural-marquise-shaped-diamond-engagement-ring-684711', '/diamonds/emerald-cut-diamond-engagement-ring-175-ct-total-diamond-weight-684691', '/diamonds/fantastic-sapphire-684606', '/diamonds/engagement-ring-center-cushion-cut-101ct-diamond-684331', '/diamonds/engagement-ring-103ct-total-diamond-weight-684336', '/diamonds/gia-certified-engagement-ring-191-ct-total-diamond-weight-684341', '/diamonds/gia-certified-engagement-ring-146-ct-total-diamond-weight-684346', '/diamonds/engagement-ring-600ct-center-green-emerald-and-two-trapezoid-diamonds-sides-684271', '/diamonds/engagement-ring-features-100ct-center-oval-diamond-684281', '/diamonds/engagement-ring-center-cushion-cut-103ct-diamond-684291', '/diamonds/elegant-engagement-ring-050ct-683406', '/diamonds/radiant-cut-yellow-diamond-engagement-ring-wedding-ring-bridal-ring-promise-ring', '/diamonds/15-cttw-princess-diamond-3-stone-bridal-engagement-ring-14k-white-gold-682196', '/diamonds/12-cttw-2-stone-diamond-hearts-together-bridal-wedding-ring-set-10k-white-gold-682181', '/diamonds/2-ctw-double-halo-diamond-engagement-ring-wedding-band-set-10k-white-gold-682191', '/diamonds/12-cttw-round-diamond-cindys-dream-bridal-engagement-ring-10k-rose-gold-682186', '/diamonds/round-brilliant-diamond-engagement-ring-682016', '/diamonds/round-diamond-engagement-ring-430-ct-total-diamond-weight-681016', '/diamonds/300-emerald-halo-engagement-ring-25-vvs2-gia-center-680626', '/diamonds/deal-day-208-carat-certified-big-look-less-value-680366', '/diamonds/gabriel-co-round-diamond-engagement-ring-679546', '/diamonds/vintage-platinum-tacori-setting-free-wedding-band-677461', '/diamonds/stunning-round-diamond-engagement-ring-set-677316', '/diamonds/gia-certified-fantastic-engagement-ring-677311', '/diamonds/gia-certified-marquise-diamond-engagement-ring-677306', '/diamonds/175-carat-diamonds-18-kt-white-gold-676816', '/diamonds/jared-princess-cut-diamond-ring-676771', '/diamonds/301-diamond-ring-wedding-set-201-i-vs1-gia-center-diamond-676456', '/diamonds/radiant-cut-beautiful-engagement-ring-676061', '/diamonds/tacori-260-diamond-ring-180-ct-emerald-gia-center-674566', '/diamonds/pear-engagement-ring-674481', '/diamonds/170-carat-certified-oval-diamond-white-gold-18-kt-674181', '/diamonds/260diamond-engagement-ring-2oo-ivs1-gia-center-673541', '/diamonds/gia-certified-300-emerald-cut-diamond-solitaire-25-vvs2-gia-certified-673386', '/diamonds/gia-certified-platinum-075ct-cushion-cut-diamond-halo-engagement-ring-597941', '/diamonds/210-carat-gia-certified-halo-ring-15ct-i-vs1-center-673241', '/diamonds/ritani-diamond-ring-270-carat-triple-exellent-center-gia-cert-672451', '/diamonds/122-f-vvs2-diamond-solitaire-white-gold-672221', '/diamonds/princess-cut-70-cts-engagement-ring-672096', '/diamonds/zales-bridal-set-modern-1-15-ct-tw-diamond-cluster-bridal-set-14k-white-gold-595336', '/diamonds/three-stone-round-diamond-engagement-ring-and-wedding-set-671261', '/diamonds/princess-cut-diamond-engagement-ring-402-ct-total-diamond-weight-671246', '/diamonds/engagement-ring-300-ct-total-diamond-weight-671251', '/diamonds/natural-diamond-eternity-band-400tdw-671076', '/diamonds/eternity-platinum-band-671086', '/diamonds/halo-style-princess-cut-engagement-ring-and-wedding-band-set-670901', '/diamonds/three-stone-engagement-set-670726', '/diamonds/natural-diamond-engagement-ring-670676', '/diamonds/stunning-three-stone-diamond-ring-670506', '/diamonds/engagement-rings-set-670511', '/diamonds/gia-certified-engagement-ring-670521', '/diamonds/amazing-tree-stone-ring-670541', '/diamonds/engagement-ring-175-ct-total-diamond-weight-video-670416', '/diamonds/rose-gold-diamond-halo-ring-670186', '/diamonds/fantastic-sapphire-ring-669026', '/diamonds/sale-diamond-rings-set-668736', '/diamonds/engagement-rings-set-668741', '/diamonds/engagement-ring-256-ct-total-diamond-weight-video-668556', '/diamonds/349-platinum-cushion-diamond-ring-309-ivvs1-gia-cushion-certified-center-diamond-668661', '/diamonds/fantastic-engagement-ring-gia-certified-664721', '/diamonds/diamond-engagement-ring-75ct-two-tapered-baguettes-664886', '/diamonds/natural-diamond-engagement-ring-135-ct-total-diamond-weight-663836', '/diamonds/white-gold-mens-wedding-band-663751', '/diamonds/classic-round-engagement-ring-250-ct-total-diamond-weight-video-663691', '/diamonds/natural-diamond-engagement-ring-video-663686', '/diamonds/natural-diamond-ring-155-ct-total-diamond-weight-663386', '/diamonds/engagement-ring-122-ct-total-diamond-weight-663261', '/diamonds/engagement-ring-270-ct-total-diamond-weight-663246', '/diamonds/engagement-ring-197-ct-total-diamond-weight-663226', '/diamonds/emerald-cut-diamond-engagement-ring-097-ct-total-diamond-weight-663191', '/diamonds/pear-shaped-engagement-ring-126-ct-total-diamond-weight-663161', '/diamonds/reduced-marquise-diamond-engagement-ring-106-carats-set-yellow-gold-601481', '/diamonds/78-8-carat-oval-eternity-band-each-660911', '/diamonds/engagement-bridal-set-185-ct-total-diamond-weight-659971', '/diamonds/engagement-ring-solitaire-110ct-princess-cut-diamond-659926', '/diamonds/big-fantastic-diamond-ring-video-659056', '/diamonds/engagement-ring-353-ct-total-diamond-weight-video-659051', '/diamonds/engagement-ring-215-ct-total-diamond-weight-video-659036', '/diamonds/diamond-halo-egagement-ring-gia-certified-203-cushion-cut-center-658491', '/diamonds/410-carat-3-stone-100-natural-old-mine-cut-antique-style-ring-gia-cert-wow-658081', '/diamonds/solitaire-engagement-ring-certified-oval-cut-diamond-657971', '/diamonds/rose-gold-solitaire-150-i-vs2-gia-center-657811', '/diamonds/engagement-ring-657696', '/diamonds/white-gold-engagement-ring-center-round-diamond-and-blue-sapphires-sides-618791', '/diamonds/wedding-band-657391', '/diamonds/eternity-band-657396', '/diamonds/round-diamond-solitaire-101-ct-white-gold-setting-cz-ring-travel-601621', '/diamonds/engagement-ring-301-ct-total-diamond-weight-637146', '/diamonds/engagement-ring-center-fancy-yellow-and-side-white-diamonds-624641', '/diamonds/engagement-ring-301-ct-total-diamond-weight-video-641621', '/diamonds/platinum-diamond-semi-mount-engagement-wedding-40-ct-side-stones-either-cushion-emerald', '/diamonds/custom-14k-white-gold-diamond-engagement-ring-1-carat-42-carat-melee-598411', '/diamonds/engagement-ring-312ct-total-diamond-weight-634736', '/diamonds/engagement-ring-110ct-total-diamond-weight-634726', '/diamonds/engagement-ring-center-100ct-round-diamond-634816', '/diamonds/engagement-ring-center-253ct-cushion-cut-diamond-and-side-diamonds-634881', '/diamonds/classic-tiffany-style-engagement-ring-635266', '/diamonds/engagement-ring-solitaire-108ct-round-cut-diamond-video-635416', '/diamonds/engagement-ring-205ct-total-diamond-weight-635011', '/diamonds/engagement-ring-solitaire-214ct-round-cut-diamond-platinum-video-626826', '/diamonds/classic-three-stone-engagement-ring-center-116ct-round-diamond-620531', '/diamonds/classic-white-gold-diamond-engagement-ring-625241', '/diamonds/155-ct-radiant-diamond-white-gold-vintage-bezel-set-eternity-engagement-ring-628066', '/diamonds/soldcharming-half-way-wedding-diamond-ring-629796', '/diamonds/soldplatinum-engagement-ring-solitaire-214ct-round-cut-diamond-video-624661', '/diamonds/cocktail-ring-550-ct-total-diamond-weight-video-640411', '/diamonds/certified-18k-white-gold-engagement-ring-features-172ct-center-round-diamond-619381', '/diamonds/engagement-ring-features-172ct-center-round-diamond-637591', '/diamonds/fantastic-diamond-blue-sapphire-ring-637751', '/diamonds/certified-18k-white-gold-engagement-ring-solitaire-170ct-princess-cut-diamond-video-644751', '/diamonds/gia-certified-diamond-engagement-ring-101-carat-princess-cut-center-gia-certified-347421', '/diamonds/incredibly-elegant-101-ct-cushion-cut-diamond-engagement-ring-14kt-white-gold-595661', '/diamonds/beautiful-color-stone-cocktail-ring-center-ruby-and-side-diamonds-623381', '/diamonds/charming-color-stone-cocktail-ring-center-blue-sapphire-and-side-diamonds-628236', '/diamonds/certified14k-white-gold-engagement-ring-center-253ct-cushion-cut-diamond-and-side-diamonds', '/diamonds/classic-cocktail-ring-features-280ct-total-white-and-black-diamonds-621386', '/diamonds/fantastic-engagement-ring-656711', '/diamonds/wedding-set-656566', '/diamonds/certified-engagement-ring-video-656576', '/diamonds/wedding-set-video-656596', '/diamonds/rose-gold-engagement-set-video-656611', '/diamonds/19-carat-ring-15-i-vs1-gia-radiant-center-gorgeous-ring-334061', '/diamonds/095-ct-princess-diamond-vs2-clarity-plus-2-wedding-bands-additional-075-carats-diamonds', '/diamonds/12-ct-round-brilliant-solitaire-diamond-engagement-ring-521126', '/diamonds/157ct-round-diamond-modern-engagement-ring-581131', '/diamonds/amazing-deal-princess-cut-engagement-ring-566046', '/diamonds/womens-fashion-ring-snake-shaped-650191', '/diamonds/292-carat-platinum-cushion-cut-solitaire-606961', '/diamonds/300-carat-gia-diamond-engagement-ring-25-center-ivs2-round-center-601051', '/diamonds/307-oval-diamond-pave-engagement-ring-gia-certified-631296', '/diamonds/310-platinum-emerald-diamond-ring-band-250-j-vvs2-gia-center-new-376636', '/diamonds/elegant-engagement-ring-center-130ct-princess-cut-diamond-623351', '/diamonds/classic-engagement-ring-features-202ct-round-cut-diamond-623616', '/diamonds/white-gold-engagement-ring-solitaire-110ct-princess-cut-diamond-623631', '/diamonds/charming-18k-white-gold-engagement-ring-features-125-ct-diamonds-628791', '/diamonds/18k-white-gold-engagement-ring-fancy-dark-gray-center-diamond-video-632716', '/diamonds/charming-120-ct-diamond-ring-632721', '/diamonds/14k-white-gold-engagement-ring-center-210ct-round-cut-diamond-619376', '/diamonds/white-gold-engagement-ring-solitaire-101ct-princess-cut-diamond-623606', '/diamonds/charming-engagement-ring-center-round-108ct-diamond-and-side-diamonds-video-623626', '/diamonds/engagement-ring-353-ct-total-diamond-weight-video-640551', '/diamonds/fashion-ring-features-center-13-mm-radius-pink-amethyst-video-640596', '/diamonds/amazing-097-ct-engagement-ring-632706', '/diamonds/delicate-rose-gold-engagement-ring-features-oval-100ct-diamond-video-621746', '/diamonds/18k-white-gold-engagement-ring-fancy-greenish-yellow-brown-center-diamond-632711', '/diamonds/classic-three-stone-diamond-engagement-ring-diamonds-sides-crafted-18k-yellow-gold-619366', '/diamonds/modern-14k-white-gold-engagement-ring-center-100ct-round-diamond-619371', '/diamonds/amazing-sapphire-655756', '/diamonds/fantastic-sapphire-655771', '/diamonds/263-halo-diamond-engagement-ring-yellow-gold-free-wedding-band-632516', '/diamonds/charming-yellow-gold-fashion-ring-video-643651', '/diamonds/engagement-ring-center-cushion-cut-103ct-diamond-video-648901', '/diamonds/engagement-ring-150ct-princess-and-round-cut-diamonds-636371', '/diamonds/certified-14k-white-gold-engagement-ring-center-166ct-cushion-cut-diamond-623451', '/diamonds/18k-white-gold-engagement-ring-fancy-brownish-yellow-center-diamond-632571', '/diamonds/video-classic-white-gold-diamond-band-643656', '/diamonds/classic-white-gold-diamond-engagement-ring-623341', '/diamonds/certified18k-white-gold-engagement-ring-center-157ct-princess-cut-diamond-623361', '/diamonds/engagement-ring-103ct-total-diamond-weight-636401', '/diamonds/14k-white-gold-engagement-ring-302ct-natural-princess-cut-diamond-629791', '/diamonds/gorgeous-115-ct-diamond-ring-632576', '/diamonds/dazzling-three-stone-engagement-ring-features-140ct-total-diamonds-620541', '/diamonds/18kt-white-gold-diamond-wedding-band-125ct-diamonds-video-643661', '/diamonds/elegant-white-gold-diamond-band-video-643666', '/diamonds/extraordinary-18k-white-gold-engagement-ring-center-125ct-round-diamond-621396', '/diamonds/fantastic-engagement-ring-center-cushion-cut-101ct-diamond-648906', '/diamonds/engagement-ring-center-cushion-cut-101ct-diamond-648911', '/diamonds/18k-white-gold-engagement-ring-features-center-100-ct-648916', '/diamonds/325-diamond-ring-305-i-vs1-ex-ex-ex-center-igi-606641', '/diamonds/63-cushion-diamond-engagement-ring-and-14kw-gold-wedding-band-655296', '/diamonds/220-scott-kay-diamond-ring-asscher-cut-ceter-gia-601831', '/diamonds/vintage-platinum-tacori-style-ring-style-wedding-band-combo-100ct-moissanite-521811', '/diamonds/200-ct-i-vs1-emerald-cut-gia-certified-pave-diamond-mounting-560271', '/diamonds/brand-new-603-platinum-diamond-ring-band-save-thousands-560986', '/diamonds/amazing-ring-150ct-ivs1center-gia-certified-solitaire-502311', '/diamonds/gia-certified-stunning-diamond-engagement-ring-654976', '/diamonds/18k-white-gold-engagement-ring-features-center-100-ct-emerald-cut-647956', '/diamonds/engagement-ring-600ct-center-green-emerald-and-two-trapezoid-diamonds-sides-648076', '/diamonds/170-plat-oval-diamond-solitaire-ring-baguettes-150-i-vs2-gia-center-certified-549386', '/diamonds/320ct-oval-pave-diamond-ring-250-j-vvs2-oval-comes-gia-certified-center-575191', '/diamonds/10000-retail-2004-jb-star-diamond-encircled-platinum-wedding-band-3565-2021-firm-nearly', '/diamonds/delicate-white-gold-engagement-ring-center-122ct-princess-cut-diamond-and-pave-diamonds', '/diamonds/engagement-ring-center-round-cut-100ct-diamond-631571', '/diamonds/certified-engagement-ring-362-ct-total-diamond-weight-video-643486', '/diamonds/engagement-ring-295-ct-total-diamond-weight-video-639366', '/diamonds/gia-certified-engagement-ring-285-ct-total-diamond-weight-video-639561', '/diamonds/platinum-engagement-diamond-ring-351ct-total-diamonds-618421', '/diamonds/yellow-gold-diamond-band-622606', '/diamonds/video-engagement-bridal-set-185-ct-total-diamond-weight-639581', '/diamonds/video-half-way-18k-white-gold-diamond-band-features-018ct-total-diamonds-639601', '/diamonds/14k-white-gold-engagement-ring-122ct-main-round-diamond-618786', '/diamonds/elegant-channel-set-diamond-engagement-ring-622591', '/diamonds/white-gold-diamond-wedding-band-622621', '/diamonds/platinum-engagement-ring-161ct-tdw-635291', '/diamonds/magnificent-gia-certified-platinum-wedding-set-216ct-diamonds-gia-certified-618446', '/diamonds/white-gold-diamond-wedding-band-622631', '/diamonds/platinum-engagement-ring-solitaire-round-cut-diamond-video-643316', '/diamonds/engagement-ring-center-cushion-cut-101ct-diamond-video-647876', '/diamonds/video-fantastic-engagement-ring-center-cushion-cut-101ct-diamond-647881', '/diamonds/amazing-050ct-round-cut-engagement-ring-video-643496', '/diamonds/platinum-engagement-three-stone-ring-312ct-total-diamond-weight-gia-certified-618416', '/diamonds/half-way-18k-white-gold-diamond-band-features-025ct-total-diamonds-video-639596', '/diamonds/beautiful-color-stone-cocktail-ring-center-blue-sapphire-and-side-diamonds-622811', '/diamonds/400-set-diamond-ring-set-250i-si1-gia-cushion-center-wedding-band-combo-630941', '/diamonds/stunning-gia-certified-080ct-i-vvs1-excellent-cut-round-stone-platinum-014ct-petite-pave', '/diamonds/modern-customized-152-carat-18kt-white-gold-amazing-deal-638281', '/diamonds/certified-engagement-ring-center-emerald-100ct-diamond-and-side-diamonds-631321', '/diamonds/diamond-eternity-band-total-042ct-round-cut-diamonds-627296', '/diamonds/diamond-eternity-band-features-320ct-round-diamonds-622286', '/diamonds/engagement-ring-center-gia-cushion-217ct-diamond-622291', '/diamonds/engagement-ring-center-pear-shape-055ct-diamond-646796', '/diamonds/elegant-and-gentle-solitaire-engagement-ring-crafted-white-gold-646831', '/diamonds/engagement-ring-center-157ct-princess-cut-diamond-634871', '/diamonds/three-stone-platinum-engagement-ring-video-643121', '/diamonds/white-gold-engagement-ring-features-030ct-five-round-cut-diamonds-622331', '/diamonds/amazing-engagement-ring-527-tdw-video-643341', '/diamonds/gorgeous-engagement-ring-334-ct-total-diamond-weight-629781', '/diamonds/tiffany-style-engagement-ring-center-round-cut-diamond-621761', '/diamonds/classic-101ct-round-engagement-ring-631281', '/diamonds/classic-engagement-ring-video-643096', '/diamonds/engagement-ring-center-round-cut-diamond-video-635411', '/diamonds/super-engagement-ring-video-643091', '/diamonds/gorgeous-100ct-round-engagement-ring-631311', '/diamonds/white-gold-engagement-ring-solitaire-025ct-round-diamond-622316', '/diamonds/engagement-ring-center-cushion-cut-103ct-diamond-647341', '/diamonds/classic-elegant-platinum-engagement-ring-053-ct-center-round-diamond-and-050-ct-side', '/diamonds/three-stone-yellow-gold-engagement-ring-features-center-050ct-round-diamond-635256', '/diamonds/engagement-ring-center-cushion-cut-diamond-635306', '/diamonds/classic-engagement-ring-center-natural-round-cut-diamond-video-635396', '/diamonds/mens-ring-275-fancy-yellow-moissanite-diamond-tension-set-ring-size-105-510666', '/diamonds/charming-engagement-ring-center-cushion-150ct-diamond-and-side-diamonds-626711', '/diamonds/amazing-engagement-ring-video-646021', '/diamonds/amazing-engagement-ring-center-100ct-radiant-cut-diamond-625426', '/diamonds/elegant-engagement-ring-center-119ct-round-cut-diamond-625871', '/diamonds/unique-14k-white-gold-diamond-ring-features-060ct-total-diamonds-626991', '/diamonds/222-pave-set-matching-band-and-122-f-vvs2-center-604661', '/diamonds/15-i-vs1-sq-emasscher-cut-gia-solitaire-601241', '/diamonds/201ct-ladies-oval-diamond-engagement-ring-150-i-vs1-gia-center-591691', '/diamonds/elegant-engagement-ring-100ct-center-green-emerald-and-two-round-diamonds-sides-video', '/diamonds/gorgeous-217ct-princess-engagement-ring-634711', '/diamonds/charming-eternity-band-179ct-round-diamonds-and-292ct-blue-sapphires-video-620856', '/diamonds/half-way-wedding-diamond-ring-634721', '/diamonds/14k-white-gold-engagement-ring-features-100-ct-center-diamond-630671', '/diamonds/platinum-eternity-band-features-215ct-total-diamonds-video-620841', '/diamonds/radiant-cut-blue-diamond-14k-wg-white-diamonds-gorgeous-641816', '/diamonds/unique-half-way-eternity-diamond-ring-060ct-diamonds-620851', '/diamonds/engagement-ring-center-100ct-radiant-cut-diamond-625421', '/diamonds/tiffany-style-white-gold-engagement-ring-solitaire-025ct-round-diamond-634686', '/diamonds/fashion-ring-372-ct-total-diamond-weigh-video-638696', '/diamonds/three-stone-engagement-ring-features-205ct-princess-cut-diamonds-630656', '/diamonds/platinum-engagement-ring-center-diamond-203ct-d-si2-asscher-cut-630686', '/diamonds/270-diamond-solitaire-gorgeous-gia-i-vs1-center-new-ring-296866', '/diamonds/gia-certified-amazing-200ct-cushion-cut-engagement-ring-video-638431', '/diamonds/250-diamond-engagement-ring-200-i-vs1-center-653516', '/diamonds/beautiful-half-way-channel-set-diamond-ring-video-629711', '/diamonds/charming-18k-white-gold-cocktail-ring-130ct-natural-diamonds-621401', '/diamonds/engagement-ring-center-157ct-princess-cut-diamond-video-642606', '/diamonds/classic-engagement-ring-features-six-princess-cut-diamonds-621741', '/diamonds/video-engagement-ring-features-105ct-princess-cut-diamonds-642646', '/diamonds/engagement-ring-features-100-ct-diamonds-video-642716', '/diamonds/classic-three-stone-yellow-gold-engagement-ring-features-center-050ct-round-diamond-621771', '/diamonds/classic-three-stone-diamond-engagement-ring-crafted-14k-yellow-goldvideo-629706', '/diamonds/beautiful-three-stone-platinum-engagement-ring-101ct-center-round-diamond-621751', '/diamonds/stunning-halo-engagement-ring-center-135ct-round-diamond-621756', '/diamonds/certified-platinum-engagement-ring-653346', '/diamonds/171-engagement-ring-gia-certified-15ct-ivs2-center-600446', '/diamonds/brand-new-diamond-engagement-halo-ring-gia-certified-center-stone-586131', '/diamonds/engagement-ring-features-150ct-total-diamond-weight-637596', '/diamonds/white-gold-engagement-ring-features-119ct-round-cut-diamond-625221', '/diamonds/rose-gold-engagement-ring-features-119ct-round-cut-diamond-625231', '/diamonds/three-stone-ring-gia-certified-652856', '/diamonds/exquisite-103ct-marquise-diamond-engagement-ring-crafted-14k-white-gold-620536', '/diamonds/eternity-diamond-band-637736', '/diamonds/diamond-eternity-band-total-250ct-round-cut-diamonds-620286', '/diamonds/engagement-ring-canter-116ct-round-diamond-641631', '/diamonds/charming-eternity-band-400ct-round-diamonds-620301', '/diamonds/fantastic-channel-set-blue-sapphires-and-diamond-band-video-629811', '/diamonds/classic-diamond-engagement-ring-video-637776', '/diamonds/rose-gold-cocktail-diamond-ring-175ct-total-diamond-weight-video-629981', '/diamonds/elegant-engagement-ring-center-certified-123ct-round-diamond-620526', '/diamonds/white-gold-engagement-ring-features-111ct-princess-cut-diamond-625216', '/diamonds/certified-189-ct-diamond-ring-633466', '/diamonds/gia-certified-engagement-rings-set-652891', '/diamonds/144-carat-fancy-yellow-oval-cut-diamond-engagement-ring-586146', '/diamonds/14k-rose-gold-diamond-engagement-ring-652021', '/diamonds/emerald-and-diamond-ring-18k-gold-509446', '/diamonds/3-stone-radiant-engagement-ring-509941', '/diamonds/twin-stone-pear-shape-ring-509441', '/diamonds/elegant-white-gold-blue-sapphire-and-diamonds-ring-651381', '/diamonds/elegant-engagement-ring-200ct-center-blue-sapphire-and-two-fancy-yellow-pear-shape-diamonds', '/diamonds/engagement-ring-old-european-cut-video-ring-644756', '/diamonds/amazing-engagement-ring-527-tdw-651091', '/diamonds/fashion-diamond-ring-637241', '/diamonds/three-stone-engagement-ring-center-234ct-round-diamond-video-628771', '/diamonds/engagement-ring-features-100ct-center-oval-diamond-637646', '/diamonds/unique-half-way-eternity-diamond-ring-624696', '/diamonds/charming-fashion-diamond-ring-637236', '/diamonds/extraordinary-engagement-ring-center-116ct-princess-cut-diamond-video-620311', '/diamonds/fantastic-090-ct-diamond-ring-633171', '/diamonds/gorgeous-100-ct-diamond-ring-633176', '/diamonds/certified-platinum-engagement-ring-center-152ct-cushion-cut-diamond-and-side-diamonds', '/diamonds/stunning-119-ct-diamond-ring-633196', '/diamonds/18k-white-gold-engagement-ring-fancy-dark-orande-brown-center-diamond-633166', '/diamonds/18k-white-gold-engagement-ring-fancy-brown-yellow-center-diamond-633181', '/diamonds/beautiful-white-gold-engagement-ring-solitaire-100ct-cushion-cut-diamond-623956', '/diamonds/beautiful-platinum-engagement-ring-center-202ct-cushion-cut-diamond-624681', '/diamonds/platinum-engagement-ring-center-301ct-cushion-cut-fancy-yellow-diamond-video-650846', '/diamonds/fantastic-engagement-ring-video-640861', '/diamonds/gorgeous-engagement-ring-256-ct-total-diamond-weight-video-636886', '/diamonds/gorgeous-white-gold-diamond-engagement-ring-153ct-tdw-video-640941', '/diamonds/14k-white-gold-engagement-ring-165-ct-total-diamond-weight-618921', '/diamonds/platinum-engagement-ring-five-round-cut-diamonds-206ct-total-diamond-weight-618796', '/diamonds/platinum-engagement-three-stone-ring-312ct-total-diamonds-gia-certified-618441', '/diamonds/14k-yellow-gold-classic-engagement-ring-center-068ct-round-diamond-618936', '/diamonds/beautiful-half-way-wedding-diamond-ring-627371', '/diamonds/three-stone-engagement-ring-100ct-center-round-diamond-629071', '/diamonds/engagement-ring-center-116ct-princess-cut-diamond-video-640961', '/diamonds/classic-engagement-ring-center-gia-cushion-217ct-diamond-619991', '/diamonds/diamond-eternity-wedding-band-total-100ct-round-cut-diamonds-627326', '/diamonds/delicate-rose-gold-engagement-ring-features-075ct-total-diamonds-622296', '/diamonds/certified-platinum-engagement-ring-415-ct-total-diamond-weight-video-640811', '/diamonds/video-certified-white-gold-engagement-ring-400-ct-total-diamond-weight-640856', '/diamonds/solitaire-engagement-ring-certified-101ct-princess-cut-diamond-619986', '/diamonds/fantastic-diamond-wedding-band-total-057ct-round-cut-diamonds-628921', '/diamonds/platinum-engagement-ring-features-103-ct-diamonds-618931', '/diamonds/charming-diamond-eternity-band-features-500ct-round-diamonds-video-629086', '/diamonds/modern-engagement-ring-150ct-total-diamond-weight-crafted-white-gold-618781', '/diamonds/fantasticagement-ring-center-301ct-cushion-cut-fancy-yellow-diamond-619796', '/diamonds/beautiful-diamond-eternity-band-features-500ct-round-diamonds-video-629076', '/diamonds/classic-half-way-wedding-diamond-band-628916', '/diamonds/yellow-gold-engagement-ring-features-118ct-total-diamond-weight-618941', '/diamonds/classic-elegant-platinum-engagement-ring-center-105-radiant-fancy-yellow-diamond-619651', '/diamonds/solitaire-rose-gold-engagement-ring-172ct-cushion-diamond-622311', '/diamonds/18k-white-gold-engagement-ring-solitaire-100ct-round-cut-diamond-631256', '/diamonds/diamond-eternity-band-features-400ct-emerald-diamonds-636811', '/diamonds/243-scott-kay-engagement-ring-203-ct-gia-cushion-enter-636856', '/diamonds/tiffany-co-d-vs1-platinum-round-engagement-ring-solitaire-502166', '/diamonds/classic-engagement-ring-cushion-cut-certified-150-carat-great-deal-637826', '/diamonds/round-brilliant-cut-engagement-ring-114ct-center-beautiful-598111', '/diamonds/custom-engagement-ring-round-diamond-120-carat-certified-641896', '/diamonds/152ct-engagement-ring-620196', '/diamonds/stunning-custom-251-tcw-gia-radiant-engagement-ring-wedding-band-630266', '/diamonds/stunning-14k-yellow-gold-engagement-diamond-ring-beautiful-gia-certified-051ct-centre', '/diamonds/069-carat-round-diamond-solitaire-engagement-ring-610826', '/diamonds/striking-2-carat-asscher-cut-engagement-ring-562791', '/diamonds/110-ct-total-weight-princess-cut-diamond-engagement-ring-562816', '/diamonds/130-ct-emerald-cut-center-diamond-engagement-ring-18kt-white-gold-562806', '/diamonds/engagement-and-wedding-band-set-517976', '/diamonds/diamond-encrusted-two-heart-engagement-ring-490681', '/diamonds/stylish-bezel-set-center-diamond-set-platinum-band-artisticaly-carved-design-both-sides-080', '/diamonds/halo-ring-features-exclusive-three-stone-design-round-cut-diamonds-platinum-setting100-ct', '/diamonds/steal-artisan-made-heirloom-6-ct-engagement-ring-306956']
# href_collect = ['/diamonds/engagement-ring-princess-cut-730826', '/diamonds/301-elongated-cushion-cut-gia-cert-lab-grown-730194', '/diamonds/gia-certified-271-ctw-3-stone-old-european-cut-ring-730193']

# href_collect = ['/diamonds/zales-celebration-diamond-collection-engagement-ring-730753',
    '/diamonds/tiffany-co-princess-cut-diamond-ring-730752',
    '/diamonds/marquise-cut-14k-yellow-gold-diamond-ring-48ct-gemstone-50ct-side-stones-730751',
    '/diamonds/kay-jewelers-round-engagement-ring-730742',
    '/diamonds/kay-jewelers-diamond-princess-cut-engagement-ring-diamond-band-730739',
    '/diamonds/zales-14k-marquise-engagement-ring-730738',
    '/diamonds/engagement-ring-and-wedding-band-730553',
    '/diamonds/beautiful-18k-white-gold-19-carat-cushion-cut-diamond-wedding-set-730740',
    '/diamonds/rose-gold-engagment-ring-w-wedding-band-730743',
    '/diamonds/engagement-ring-%C3%A9tincelle-cartier-730746',
    '/diamonds/diamond-vault-65-solitaire-730748',
    '/diamonds/elegant-classy-15-carat-platinum-engagement-ring-730736',
    '/diamonds/deal-wont-last-123-carat-vintage-cushion-cut-diamond-white-gold-mounting-730735',
    '/diamonds/great-deal-171-carat-diamond-saphire-ring-white-gold-730734',
    '/diamonds/111-ct-princess-cut-diamond-engagement-ring-730737',
    '/diamonds/p%E1%B4%80s%E1%B4%9B-p%CA%80%E1%B4%87s%E1%B4%87%C9%B4%E1%B4%9B-f%E1%B4%9C%E1%B4%9B%E1%B4%9C%CA%80%E1%B4%87-p%CA%80%C9%AA%C9%B4%E1%B4%84%E1%B4%87ss-c%E1%B4%9C%E1%B4%9B-730731',
    '/diamonds/opal-and-diamond-engagement-set-730732',
    '/diamonds/valina-wedding-set-730730',
    '/diamonds/120-ct-radiant-gia-certified-engagement-ring-564371',
    '/diamonds/260ct-blue-nile-engagement-ring-730606',
    '/diamonds/james-allen-emerald-cut-diamond-and-platinum-engagement-ring-730725',
    '/diamonds/jared-14k-white-gold-engagement-ring-and-band-730724',
    '/diamonds/213-ct-solitaire-round-diamond-730723',
    '/diamonds/solitaire-round-brilliant-diamond-engagement-ring-730728',
    '/diamonds/vera-wang-bridal-set-730722',
    '/diamonds/314ct-round-brilliant-engagement-ring-fancy-pink-side-diamonds-egl-certified-incredible',
    '/diamonds/whitehall-jewelers-125-ct-wedding-set-730717',
    '/diamonds/4-quad-princess-cut-bridal-set-730721',
    '/diamonds/zales-engagement-ring-730720',
    '/diamonds/wedding-band-730718',
    '/diamonds/moissanite-engagement-ring-730716',
    '/diamonds/neil-lane-wedding-ring-and-band-730713',
    '/diamonds/certified-tanzanite-diamond-round-platinum-950-123ct-double-halo-engagement-ring-730714',
    '/diamonds/050ct-igi-certified-forever-diamond-engagement-ring-18k-white-gold-uk-hallmarked-730715',
    '/diamonds/tolkowsky-ideal-cut-diamond-set-platinum-engagement-ring-730712',
    '/diamonds/jared-730711',
    '/diamonds/split-pave-band-cushion-cut-engagement-ring-730709',
    '/diamonds/engagement-ring-730710',
    '/diamonds/beautiful-round-diamond-over-3-carats-730706',
    '/diamonds/heart-diamond-engagement-ring-730705',
    '/diamonds/diamonds-direct-stunning-cushion-cut-solitaire-engagement-ring-platinum-730702',
    '/diamonds/zales-wedding-ring-wedding-band-sale-730701',
    '/diamonds/custom-marquise-engagement-ring-730698',
    '/diamonds/princess-cut-engagement-ring-730697',
    '/diamonds/205-ct-solitaire-round-brilliant-diamond-ring-730696',
    '/diamonds/155-ct-round-brilliant-solitaire-diamond-ring-730695',
    '/diamonds/unique-green-diamond-engagement-ring-730693',
    '/diamonds/ladie%E2%80%99s-diamond-engagement-ring-730689',
    '/diamonds/platinum-diamond-solitaire-ring-5-carat-730688',
    '/diamonds/custom-made-ladies-platinum-sapphire-and-diamond-three-stone-ring-730683',
    '/diamonds/2-ct-diamond-solitaire-730684',
    '/diamonds/gold-round-centermarquise-side-diamond-ring-730678',
    '/diamonds/round-moissanite-pave-engagement-ring-730679',
    '/diamonds/princess-cut-engagement-ring-2-carats-730667',
    '/diamonds/85-carat-radiant-cut-ring-custom-made-730682',
    '/diamonds/stunning-solitaire-masterpiece-730671',
    '/diamonds/round-brilliant-ring-730676',
    '/diamonds/engagement-ring-sale-730672',
    '/diamonds/ladys-14kt-rose-gold-pear-shaped-engagement-ring-730669',
    '/diamonds/princess-cut-engagement-ring-2-carats-730666',
    '/diamonds/moissanite-princess-cut-diamond-2ctw-950-platinum-art-deco-engagement-ring-730664',
    '/diamonds/tiffany-diamond-730665',
    '/diamonds/helzberg-14k-engagementwedding-band-set-my-loss-your-gain-730668',
    '/diamonds/princess-cut-diamond-halo-top-hidden-sapphires-custom-engagement-ring-196-total-cts-730674',
    '/diamonds/na-hoku-diamond-engagement-ring-730675',
    '/diamonds/vera-wang-love-collection-1-13-ct-tw-emerald-cut-diamond-double-frame-engagement-ring-14k',
    '/diamonds/james-allen-067-carat-brilliant-pear-engagement-ring-14k-white-gold-730662',
    '/diamonds/jared-14k-platinum-engagement-ring-wedding-band-730660',
    '/diamonds/recycled-14k-gold-engagement-ring-floating-diamond-prong-730659',
    '/diamonds/tiffany-co-137-vs1-g-730656',
    '/diamonds/jaffe-wedding-set-sale-730655',
    '/diamonds/tacori-engagement-ring-730653',
    '/diamonds/101-diamond-ring-730652',
    '/diamonds/halo-diamond-engagement-ring-730650',
    '/diamonds/oval-halo-12-ct-center-stone-gia-certified-730649',
    '/diamonds/204-carat-cushion-cut-halo-730603',
    '/diamonds/past-present-future-ring-730646',
    '/diamonds/helzberg-masterpiece-wedding-set-730640',
    '/diamonds/black-hills-gold-wedding-set-730644',
    '/diamonds/hearts-eternity-bridal-set-730643',
    '/diamonds/zales-elegant-vintage-style-round-cut-diamond-engagement-ring-730642',
    '/diamonds/310-emerald-cut-diamond-ring-730635',
    '/diamonds/round-diamond-wedding-set-730631',
    '/diamonds/timeless-cushion-cut-ring-730630',
    '/diamonds/stunning-infinity-diamond-ring-730629',
    '/diamonds/beautiful-custom-designed-anniversary-ring-730627',
    '/diamonds/discounted-new-wedding-set-730626',
    '/diamonds/engagement-and-wedding-band-set-730625',
    '/diamonds/forever-one-moissanite-engagement-ring-730624',
    '/diamonds/princess-cut-14kw-3-stone-ring-116ct-tw-730623',
    '/diamonds/801-round-brilliant-engagement-ring-730618',
    '/diamonds/solitaire-engagement-ring-730622',
    '/diamonds/vintage-style-tacori-engagement-ring-730621',
    '/diamonds/round-brilliant-diamond-18k-yellow-gold-band-and-platinum-6-prong-setting-730619',
    '/diamonds/brilliant-earth-18k-white-gold-twilight-lab-diamond-ring-moissanite-size-65-730616',
    '/diamonds/125-tcw-platinum-princess-cut-engagement-ring-d-color-matching-wedding-band-730615',
    '/diamonds/14-karat-white-gold-diamond-engagement-ring-730614',
    '/diamonds/rose-gold-round-diamond-engagement-ring-730608',
    '/diamonds/engagement-ring-purchased-never-proposed-730605',
    '/diamonds/round-brilliant-cut-diamond-730604',
    '/diamonds/princess-shaped-wedding-ring-set-730602',
    '/diamonds/2-carat-eternity-band-white-gold-730601',
    '/diamonds/diamonds-direct-princess-cut-engagement-ring-730599',
    '/diamonds/halo-bridal-set-730598',
    '/diamonds/205-tcw-bespoke-emerald-engagement-ring-162-ctw-center-stone-w-diamond-baguette-prongs',
    '/diamonds/2-%C2%BD-ct-round-solitaire-diamond-engagement-ring-730591',
    '/diamonds/james-allen-round-diamond-engagement-ring-730588',
    '/diamonds/round-diamond-engagement-ring-730587',
    '/diamonds/tiffany-co-solitaire-diamond-ring-730585',
    '/diamonds/ladies-14kt-two-tone-gold-diamond-and-sapphire-ring-730584',
    '/diamonds/forevermark-engagement-ring-730563',
    '/diamonds/unique-setting-75-center-round-diamond-730581',
    '/diamonds/10kw%E2%80%9Drd-dia-wbl-sappi-730573',
    '/diamonds/round-brilliant-ring-your-dreams-730580',
    '/diamonds/beautiful-oval-diamond-ring-730578',
    '/diamonds/last-chance-round-brilliant-1-carat-diamond-engagement-ring-leo-collection-jared-730577',
    '/diamonds/diamond-and-sapphire-ring-fair-market-value-730568',
    '/diamonds/engagement-wedding-band-combo-730566',
    '/diamonds/white-gold-diamond-engagement-ring-730564',
    '/diamonds/hearts-fire-engagement-ring-and-wedding-band-730561',
    '/diamonds/beautiful-art-deco-style-engagement-ring-sale-730560',
    '/diamonds/tacori-wedding-set-730558',
    '/diamonds/round-cut-engagement-ring-07-ct-i1-clarity-g-color-730556',
    '/diamonds/blue-nile-custom-engagement-ring-high-quality-single-diamond-730555',
    '/diamonds/custom-made-90ct-cushion-cut-diamond-ring-730552',
    '/diamonds/zales-engagement-ring-band-730551',
    '/diamonds/forevermark-briliant-white-gold-engagement-ring-520976',
    '/diamonds/solitaire-engagement-ring-730549',
    '/diamonds/072-carat-princess-cut-engagement-ring-543191',
    '/diamonds/verragio-venetian-collection-full-set-all-excellent-condition-includes-side-stone-semi',
    '/diamonds/258-carat-diamond-solitaire-730538',
    '/diamonds/tiffany-solitaire-ring-730534',
    '/diamonds/jareds-engagement-ring-wrapping-bands-730533',
    '/diamonds/kay-jewelers-14k-diamond-ring-and-band-730532',
    '/diamonds/jared-new-14k-white-gold-90-carat-diamond-engagement-ring-matching-wedding-band-730530',
    '/diamonds/jared-pear-shape-diamond-14k-yellow-gold-wedding-rings-730527',
    '/diamonds/2ctw-split-shank-halo-engagement-ring-baguette-wedding-band-728295',
    '/diamonds/205-ct-lab-grown-round-brilliant-diamond-ring-730529',
    '/diamonds/197-carat-center-stone-271-carat-total-tiffany-co-platinum-and-diamond-engagement-ring',
    '/diamonds/timeless-282-tcw-radiant-cut-diamond-ring-730521',
    '/diamonds/engagement-ring-and-wedding-band-730520',
    '/diamonds/18-total-carat-rose-gold-oval-diamond-engagement-ring-730518',
    '/diamonds/ladies-151-carat-yellow-gold-six-prong-solitaire-engagement-ring-730516',
    '/diamonds/lab-grown-155-ct-round-brilliant-diamond-engagement-ring-730517',
    '/diamonds/wedding-and-engagement-bands-730514',
    '/diamonds/104ct-natural-ruby-and-diamond-halo-ring-platinum-orianne-collins-730512',
    '/diamonds/kay-jewelers-bridal-set-730511',
    '/diamonds/rare-and-different-287-carat-diamond-ring-cushion-cut-diamond-deal-day-730509',
    '/diamonds/great-deal-511-carat-diamond-ring-princess-cut-platinum-setting-style-730508',
    '/diamonds/lab-grown-251ct-round-brilliant-diamond-ring-730515',
    '/diamonds/diamond-and-aquamarine-engagement-ring-730506',
    '/diamonds/verragio-exquisite-engagement-ring-2-woman%E2%80%99s-wedding-bands-and-men%E2%80%99s-wedding-band-730503',
    '/diamonds/pear-shaped-engagement-ring-730498',
    '/diamonds/princess-cut-diamond-engagement-ring-730501',
    '/diamonds/diamond-ring-appraised-3k-730485',
    '/diamonds/simond-g-halo-diamond-ring-730484',
    '/diamonds/kay-jewelers-women%E2%80%99s-2-tone-1-ct-bridal-set-730479',
    '/diamonds/rose-gold-anniversary-or-engagement-ring-730472',
    '/diamonds/2ct8mm-round-moissanite-petite-cushion-halo-engagement-ring-730478',
    '/diamonds/brilliant-round-solitaire-diamond-engagement-ring-yellow-gold-band-730473',
    '/diamonds/marquise-cut-beautiful-ring-730441',
    '/diamonds/three-stone-diamond-engagement-ring-730439',
    '/diamonds/forevermark-halo-diamond-engagement-ringprice-dropped-730003',
    '/diamonds/jared-jewelers-round-brilliant-classic-engagement-ring-730431',
    '/diamonds/zales-wedding-ring-set-730430',
    '/diamonds/65-carat-platinum-cushion-cut-moon-sides-engagement-ring-730419',
    '/diamonds/brilliant-earth-solitaire-moissanite-engagement-ring-730415',
    '/diamonds/kay-jewelers-engagement-set-730413',
    '/diamonds/custom-design-princess-cut-size-675-730409',
    '/diamonds/061ct-igi-certified-h-vs1-platinum-princess-engagement-ring-730407',
    '/diamonds/white-gold-halo-style-princess-cut-wedding-set-730396',
    '/diamonds/custom-crafted-engagement-ring-featuring-prong-set-round-moissanite-center-stone-flanked',
    '/diamonds/lab-grown-emerald-cut-engagement-ring-730400',
    '/diamonds/tacori-dantela-2-carat-730333',
    '/diamonds/halo-engagement-ring-730379',
    '/diamonds/natalie-k-diamond-ring-200-carat-total-730380',
    '/diamonds/gia-certified-e-color-3-stone-princess-cut-engagement-ring-wedding-band-730375',
    '/diamonds/066ct-round-diamond-halo-engagement-ring-wedding-ring-bridal-set-18k-white-gold-730361',
    '/diamonds/45-asscher-cut-sides-diamond-ring-730359',
    '/diamonds/leo-cut-diamond-wedding-set-730356',
    '/diamonds/new-486-carat-pear-cut-3-stone-diamond-ring-730345',
    '/diamonds/helzberg%E2%80%99s-gorgeous-round-brillant-wedding-ring-730334',
    '/diamonds/sholdt-design-solitaire-engagement-ring-size-7-091-carat-730326',
    '/diamonds/215-ct-vs2-round-solitaire-engagement-ring-730309',
    '/diamonds/4-carat-diamond-ring-35-radiant-cut-center-730311',
    '/diamonds/318-carat-wedding-set-218-ivs2-triple-excellent-730317',
    '/diamonds/57-carat-oval-stunner-730312',
    '/diamonds/vera-wang-love-diamond-ring-730298',
    '/diamonds/141-total-ct-diamond-engagementwedding-ring-set-appraised-4250-15-years-ago-730290',
    '/diamonds/140-ctw-round-brilliant-diamond-engagement-ring-730297',
    '/diamonds/83-antique-style-engagement-ring-730279',
    '/diamonds/custom-claddagh-ring-730270',
    '/diamonds/kay-jewelers-diamond-solitaire-engagement-ring-1-ct-tw-princess-cut-10k-white-gold-730271',
    '/diamonds/round-brilliant-diamond-ring-wedding-set-730276',
    '/diamonds/267ct-round-brilliant-lab-grown-diamond-ring-730275',
    '/diamonds/80ct-princess-cut-diamond-halo-ring-730273',
    '/diamonds/zales-14k-white-gold-quad-princess-cut-engagement-ring-730253',
    '/diamonds/zales-love%E2%80%99s-destiny-engagement-ring-730252',
    '/diamonds/helzberg-limited-edition-style-engagement-ring-princess-cut-white-gold-730239',
    '/diamonds/engagement-setting-not-including-center-diamond-730237',
    '/diamonds/1-ct-spiral-halo-vera-wang-love-collection-sapphire-mounting-730234',
    '/diamonds/12-ct-antique-style-diamond-engagement-wedding-ring-set-sapphires-14k-white-gold-designer',
    '/diamonds/gia-certified-058ct-d-vvs1-xxx-diamond-platinum-solitaire-engagement-ring-730224',
    '/diamonds/317ct-igi-certified-emerald-diamond-ring-platinum-18k-gold-new-730225',
    '/diamonds/new-254ct-hrd-certified-vvs1-diamond-tiffany-co-style-platinum-solitaire-engagement-ring',
    '/diamonds/new-101ct-igi-certified-vs1-emerald-diamond-tiffany-style-platinum-solitaire-engagement',
    '/diamonds/103ct-gia-certified-platinum-princess-diamond-halo-engagement-ring-halo-730228',
    '/diamonds/050ct-gia-igi-certified-platinum-round-diamond-solitaire-engagement-ring-730229',
    '/diamonds/050ct-gia-certified-f-si1-xxx-excellent-cut-diamond-platinum-halo-engagement-ring-730230',
    '/diamonds/certified-071ct-h-si1-diamond-platinum-solitaire-engagement-ring-730231',
    '/diamonds/025ct-pear-cut-diamond-solitaire-engagement-ring-14k-yellow-gold-730214',
    '/diamonds/305-traditional-tiffany-style-diamond-ring-yellow-gold-plat-head-igi-cerified-ring-730218',
    '/diamonds/97ct-princess-cut-diamond-engagement-ring-wedding-band-set-730205',
    '/diamonds/gorgeous-neil-lane-wedding-set-730182',
    '/diamonds/platinum-033ct-certified-princess-diamond-solitaire-engagement-ring-730178',
    '/diamonds/116tcw-rachael-engagement-ring-ken-and-dana-design-730167',
    '/diamonds/543-carat-diamond-ring-730166',
    '/diamonds/leo-princess-cut-w-sapphire-stones-engagement-ring-730154',
    '/diamonds/343-carat-diamond-ring-amazing-ring-see-video-730157',
    '/diamonds/233-tacori-engagement-ring-177-g-vs1-center-730145',
    '/diamonds/07-carat-engagement-ring-two-bands-730136',
    '/diamonds/460-yellow-gold-cushion-solitaire-730114',
    '/diamonds/diamond-three-stone-engagement-ring-toby-rhinehart-design-730090',
    '/diamonds/zei-engagement-ring-730019',
    '/diamonds/two-row-139-tcw-round-diamond-wedding-ring-730077',
    '/diamonds/99-ct-princess-cut-engagement-ring-730076',
    '/diamonds/120-ctw-three-stone-diamond-ring-730075',
    '/diamonds/beautiful-princess-cut-diamond-engagement-wedding-ring-730072',
    '/diamonds/beautiful-engagement-wedding-ring-set-730074',
    '/diamonds/diamond-engagement-ring-marquise-cut-yellow-and-white-gold-matching-diamond-ring-guard',
    '/diamonds/diamond-wedding-ring-730026',
    '/diamonds/stunning-161-ct-194-tcw-brilliant-earth-engagement-ring-730006',
    '/diamonds/202-ct-cushion-benz-14k-white-gold-setting-w-5ct-band-730001',
    '/diamonds/gorgeous-round-cut-151-ct-engagement-ring-729985',
    '/diamonds/2-carat-total-weight-diamond-band-or-anniversary-ring-729983',
    '/diamonds/round-bypass-channel-moissanite-engagement-ring-729970',
    '/diamonds/new-loose-pink-diamond-151-carats-video-link-igi-certified-rose-gold-ring-729933',
    '/diamonds/michael-m-wedding-rings-set-729932',
    '/diamonds/tiffany-co-lucida-diamond-platinum-ring-729929',
    '/diamonds/249ct-egl-certified-g-vs2-platinum-bridal-set-bespoke-729900',
    '/diamonds/140ct-gia-certified-cushion-halo-engagement-ring-18k-white-gold-729913',
    '/diamonds/176ct-igi-certified-marquise-halo-14k-white-gold-engagement-ring-729909',
    '/diamonds/120ct-gia-round-halo-engagement-ring-18k-white-gold-james-allen-729911',
    '/diamonds/video-gia-certified-200ct-tiffany-co-style-round-k-vs2-excellent-cut-diamond-18k-yellow',
    '/diamonds/130ct-egl-usa-certified-round-diamond-engagement-ring-14k-white-gold-729912',
    '/diamonds/102ct-agsl-certified-i-si2-round-solitaire-14k-white-gold-engagement-ring-729902',
    '/diamonds/125ct-gia-certified-f-vvs2-round-accent-engagement-ring-18k-white-gold-729905',
    '/diamonds/157ct-certified-princess-diamond-platinum-engagement-ring-729906',
    '/diamonds/tacori-bridal-set-platinum-engagement-ring-wedding-ring-729907',
    '/diamonds/169ct-egl-usa-certified-cushion-halo-engagement-ring-14k-white-gold-729910',
    '/diamonds/143ct-gia-certified-f-vvs1-princess-trilogy-engagement-ring-platinum-729908',
    '/diamonds/video-new-gia-certified-tiffany-co-style-101ct-f-vs1-xxx-diamond-platinum-solitaire',
    '/diamonds/141ct-gia-certified-e-si2-platinum-princess-trilogy-ring-729901',
    '/diamonds/video-gia-certified-tiffany-co-style-100ct-d-vs2-diamond-platinum-solitaire-engagement-ring',
    '/diamonds/classic-vintage-diamond-bypass-ring-729879',
    '/diamonds/tacori-engagement-ring-729871',
    '/diamonds/video-tiffany-and-co-platinum-075ct-diamond-lucida-cut-radiant-square-princess-asscher',
    '/diamonds/jared-engagement-ring-3-carat-729838',
    '/diamonds/500-ct-moisanite-diamond-ring-729827',
    '/diamonds/asscher-cut-diamond-ring-25-i-vs1-gia-729833',
    '/diamonds/1-ctw-double-halo-diamond-engagement-ring-wedding-band-set-10k-white-gold-725396',
    '/diamonds/15-carat-diamond-round-cut-double-halo-engagement-ring-set-10k-white-gold-728659',
    '/diamonds/diamonds-direct-14-karat-white-gold-3-stone-engagement-ring-729804',
    '/diamonds/630-ct-radiant-diamond-729798',
    '/diamonds/1ct-tacori-halo-diamond-engagement-ring-and-band-729771',
    '/diamonds/engagement-ring-10-ct-729756',
    '/diamonds/fancy-yellow-diamond-ring-729736',
    '/diamonds/diamond-ring-729735',
    '/diamonds/tanzanite-heart-and-diamond-ring-729734',
    '/diamonds/citrine-and-diamond-ring-729733',
    '/diamonds/636-carat-round-diamond-ring-729739',
    '/diamonds/gia-certified-85-radiant-14k-gold-custom-bridal-ring-set-729730',
    '/diamonds/tiffany-cushion-cut-101-ct-white-14-karat-engagement-ring-18-karat-full-anniversary',
    '/diamonds/313-carat-diamond-engagement-ring-263-j-si1-ex-ex-ex-center-729699',
    '/diamonds/jared-cushion-cut-diamond-engagement-ring-729697',
    '/diamonds/jared-116-05-ct-princess-cut-solitaire-engagement-ring-729670',
    '/diamonds/diamonds-direct-251c-gia-certified-princess-cut-solitaire-engagement-ring-679471',
    '/diamonds/james-allen-3-ct-oval-lab-grown-diamond-engagement-ring-729679',
    '/diamonds/109ct-engagement-ring-14k-white-gold-simple-setting-thin-band-size-7-729644',
    '/diamonds/461-carat-cushion-solitaire-729639',
    '/diamonds/14-kt-white-gold-halo-style-engagement-ring-729638',
    '/diamonds/classic-five-stone-engagement-ring-features-185ct-total-diamonds-620861',
    '/diamonds/impressive-gia-certified-engagement-ring-center-076ct-pear-shape-fancy-yellow-diamond',
    '/diamonds/verragio-insignia-engagement-ring-wedding-band-729589',
    '/diamonds/huge-bling-statement-ring-hand-made-nyc-638716',
    '/diamonds/gia-certified-engagement-ring-611-carat-yellow-cushion-cut-diamond-659791',
    '/diamonds/267-carat-fancy-yellow-radiant-cut-diamond-engagement-ring-platinum-659786',
    '/diamonds/custom-moissanite-platinum-engagement-ring-729529',
    '/diamonds/egl-usa-certified-222ct-fancy-yellow-18k-white-gold-diamond-halo-engagement-ring-brand-new',
    '/diamonds/2-ctw-double-halo-diamond-engagement-ring-wedding-band-set-10k-white-gold-725401',
    '/diamonds/385ct-natural-vvs-indocilite-bi-color-blue-tourmaline-722971',
    '/diamonds/tiffany-style-legacy-aquamarinediamond-ring-729433',
    '/diamonds/pear-shape-diamond-ring-342-carat-18kt-white-gold-certified-729408',
    '/diamonds/346-ct-pear-diamond-ring-729406',
    '/diamonds/jared-princess-engagementwedding-set-729404',
    '/diamonds/14k-gold-black-and-white-diamond-ring-729402',
    '/diamonds/round-diamond-807-carat-great-deal-729348',
    '/diamonds/wow-pear-shape-diamond-681-carat-certified-729347',
    '/diamonds/great-deal-round-custom-made-diamond-ring-305-carat-hand-crafted-18kt-white-gold-729341',
    '/diamonds/beautiful-diamond-ring-171-carat-diamond-ring-deal-wont-last-729343',
    '/diamonds/rare-and-different-177-carat-diamond-ring-cushion-cut-diamond-729342',
    '/diamonds/253-cushion-solitaire-diamond-ring-729335',
    '/diamonds/custom-carved-wrap-style-engagement-ring-729334',
    '/diamonds/1ct-fancy-deep-yellowish-brown-engagement-ring-729313',
    '/diamonds/149-ct-round-diamond-ring-729261',
    '/diamonds/platinum-sapphire-and-diamond-engagement-ring-729254',
    '/diamonds/611-carat-platinum-halo-cushion-diamond-engagement-ring-729228',
    '/diamonds/jb-star-design-halo-engagement-ring-729201',
    '/diamonds/wow-deal-wont-last-631-carat-diamond-ring-certified-all-custom-made-729175',
    '/diamonds/gabriel-co-gorgeous-131-carat-marquise-diamond-engagement-ring-729186',
    '/diamonds/65-carat-wedding-set-matching-band-729154',
    '/diamonds/theo-fennell-540ct-asscher-cut-diamond-engagement-ring-18k-white-gold-727066',
    '/diamonds/neil-lane-engagement-ring-729133',
    '/diamonds/stunning-new-182ct-certified-diamond-engagement-ring-matching-wedding-band-729106',
    '/diamonds/144-ct-diamond-ring-18k-white-gold-729083',
    '/diamonds/35-assscher-cut-platinum-pave-diamond-engagement-ring-728937',
    '/diamonds/ritani-3-band-halo-ring-2-carat-ivs1-gia-center-728942',
    '/diamonds/170-oval-halo-diamond-ring-728929',
    '/diamonds/455-diamond-set-305-i-vs1-center-728926',
    '/diamonds/brand-new-650-carat-wedding-set-eternity-band-728925',
    '/diamonds/stunning-round-diamond-engagement-ring-2018-728867',
    '/diamonds/white-gold-wedding-set-tons-sparkle-728869',
    '/diamonds/engagement-ring-diamond-wedding-band-jacket-728716',
    '/diamonds/engagement-ring-71-vs2-f-gia-728814',
    '/diamonds/230-ct-gia-certified-center-diamond-pear-shape-g-color-vvs1-clarity-excellent-cut-polish',
    '/diamonds/diamond-cluster-halo-ring-717481',
    '/diamonds/10k-gold-diamond-engagement-ring-717476',
    '/diamonds/brilliant-earth-stunning-breathtaking-eco-friendly-diamond-ring-728768',
    '/diamonds/15-diamond-yellow-gold-728681',
    '/diamonds/three-piece-engagement-ring-and-wedding-bands-728634',
    '/diamonds/521-carat-platinum-custom-made-728630',
    '/diamonds/reeds-jewelers-kleinfeld-alwyn-engagement-ring-728569',
    '/diamonds/201-carat-round-excellentideal-cut-e-colorless-vvs2-clarity-6-prong-tiffany-style-14k-white',
    '/diamonds/220-carat-diamond-solitaire-ring-180-carat-center-728257',
    '/diamonds/045ct-gia-certified-d-si1-excellent-cut-halo-diamond-engagement-ring-18k-gold-728240',
    '/diamonds/185ctw-round-engagement-ring-727936',
    '/diamonds/175ctw-pear-halo-diamond-engagement-ring-727921',
    '/diamonds/125ctw-diamond-oval-engagement-ring-727916',
    '/diamonds/162-ctw-round-engagement-ring-727911',
    '/diamonds/150ctw-round-twisted-diamond-engagement-ring-727906',
    '/diamonds/150-ctw-halo-round-engagement-ring-727901',
    '/diamonds/150-ctw-round-halo-diamond-ring-727891',
    '/diamonds/14k-white-gold-engagement-ring-727861',
    '/diamonds/52-vs2-marquise-72ctw-g-color-engagement-ring-727851',
    '/diamonds/150-ctw-round-diamond-halo-engagement-ring-727796',
    '/diamonds/130-ctw-diamond-engagement-ring-727786',
    '/diamonds/112-ctw-diamond-engagement-ring-727771',
    '/diamonds/1ct-diamond-engagement-ring-727756',
    '/diamonds/130-ctw-halo-diamond-engagement-ring-727661',
    '/diamonds/125-ctw-diamond-engagement-ring-727656',
    '/diamonds/120-ctw-halo-engagement-ring-727651',
    '/diamonds/1-15-ctw-halo-diamond-engagment-ring-727646',
    '/diamonds/lab-grown-34-cttw-diamond-engagement-ring-727641',
    '/diamonds/canadian-maple-leaf-diamonds-e-vs2-halo-platinum-engagement-ring-727541',
    '/diamonds/220ct-gia-certified-platinum-cushion-diamond-halo-engagement-ring-727391',
    '/diamonds/140ct-certified-e-vvs1-marquise-platinum-bridal-engagement-ring-727386',
    '/diamonds/gia-certified-216ct-fancy-yellow-diamond-platinum-bridal-set-727376',
    '/diamonds/custom-14k-white-gold-diamond-and-moissanite-engagement-ring-set-wedding-bands-726866',
    '/diamonds/igi-certified-22k-yellow-gold-145ct-deep-blue-sapphire-and-diamond-halo-cluster-dress-ring',
    '/diamonds/engagementwedding-ring-726331',
    '/diamonds/2-ct-certified-oval-moissanite-oval-solitaire-engagement-ring-14k-yellow-gold-726061',
    '/diamonds/112ct-gia-certified-f-vvs2-cushion-cut-diamond-engagement-ring-14k-white-gold-725846',
    '/diamonds/089ct-gia-certified-e-vvs1-blue-nile-petite-twist-princess-diamond-engagement-ring-14k',
    '/diamonds/unique-round-brilliant-diamond-ring-set-14kt-white-gold-725811',
    '/diamonds/060-ct-round-brilliant-diamond-engagement-ring-725806',
    '/diamonds/145-ctw-emerald-cut-diamond-engagement-ring-725801',
    '/diamonds/brilliant-cut-solitaire-engagement-ring-wedding-band-725706',
    '/diamonds/kay-jewelers-diamond-engagement-ring-wenhancer-band-725691',
    '/diamonds/081ct-gia-certified-fancy-orange-diamond-ring-white-gold-mens-gents-unisex-725411',
    '/diamonds/081ct-gia-certified-scott-kay-round-diamond-solitaire-engagement-ring-724771',
    '/diamonds/gia-certified-094-g-si2-oval-cut-diamond-halo-engagement-ring-18k-white-gold-brilliant',
    '/diamonds/gia-certified-princess-cut-diamond-halo-engagement-ring-14k-gold-diamonds-direct-724761',
    '/diamonds/gia-certified-148ct-princess-cut-diamond-accent-engagement-ring-18k-gold-724751',
    '/diamonds/gia-certified-075ct-e-vs1-princess-cut-diamond-engagement-ring-14k-white-gold-724766',
    '/diamonds/tiffany-co-certified-118ct-classic-round-diamond-accent-engagement-ring-platinum-724776',
    '/diamonds/gia-certified-071ct-princess-cut-diamond-engagement-ring-14k-gold-724756',
    '/diamonds/igi-certified-g-vs1-163ct-round-diamond-accent-engagement-ring-wedding-ring-bridal-set-18k',
    '/diamonds/ags-certified-128ct-platinum-halo-round-diamond-engagement-ring-ben-bridge-724796',
    '/diamonds/gia-certified-209ct-round-diamond-14k-yellow-gold-solitaire-engagement-ring-wedding-ring',
    '/diamonds/gia-certified-128ct-princess-cut-diamond-accent-engagement-ring-14k-gold-diamonds-direct',
    '/diamonds/gia-certified-098ct-diamond-engagement-ring-14k-yellow-gold-724786',
    '/diamonds/056ct-igi-certified-emerald-cut-diamond-engagement-ring-18k-white-gold-rox-724846',
    '/diamonds/234ct-natural-tanzanite-and-diamond-platinum-950-bespoke-statement-dress-ring-724506',
    '/diamonds/corona-situation-classic-diamond-ring-162-carat-certified-split-shank-setting-style-724446',
    '/diamonds/video-igi-certified-d-vs2-18k-white-gold-oval-diamond-halo-engagement-ring-723721',
    '/diamonds/95-ctw-75-center-si-round-brilliant-723551',
    '/diamonds/emerald-cut-diamond-ring-723081',
    '/diamonds/14-kw-14-ct-echo-round-solitaire-brilliant-cut-diamond-engagement-ring-722406',
    '/diamonds/tourneau-de-beers-18k-gold-5-ct-solitaire-vs1-diamond-engagement-ring-722271',
    '/diamonds/222-carat-2-piece-ring-set-122-f-vvs2-ex-ex-ex-diamond-center-722251',
    '/diamonds/princess-cut-engagement-ring-wedding-band-set-size-7-722186',
    '/diamonds/beverly-k-design-18k-wg-halo-style-diamond-ring-size-6-round-brilliant-cut-center-diamond',
    '/diamonds/solitaire-princess-cut-kay-jewelers-721786',
    '/diamonds/200-oval-pave-diamond-ring-719381',
    '/diamonds/145-carat-lab-diamond-engagement-ring-14k-yellow-gold-band-721556',
    '/diamonds/video-025ct-hearts-fire-ags-certified-platinum-engagement-diamond-ring-721216',
    '/diamonds/engagement-ring-3-stunning-diamonds-coronet-setting-18-carat-gold-main-diamond-497-mm-g-si1',
    '/diamonds/290-emerald-cut-platinum-ring-720501',
    '/diamonds/great-deal-corona-situation-157-carat-diamond-ring-custom-made-certified-gemologist-720466',
    '/diamonds/lauren-b-radiant-halo-engagement-ring-14kt-white-gold-moissanite-diamond-halo-sz-5-720391',
    '/diamonds/video-110ct-natural-blue-sapphire-marquise-diamond-halo-18k-engagement-ring-720146',
    '/diamonds/james-allen-ladies-14k-white-gold-halo-diamond-engagement-ring-720042',
    '/diamonds/beautiful-sparkling-princess-cut-diamond-wedding-set-689096',
    '/diamonds/video-igi-certified-%E2%80%9Cleo-diamond%E2%80%9D-18k-white-gold-051ct-diamond-solitaire-round-brilliant',
    '/diamonds/video-gia-certified-092ct-solitaire-platinum-950-f-si1-square-princess-cut-diamond',
    '/diamonds/video-tacori-style-18k-white-gold-020ct-diamond-round-brilliant-vintage-accent-engagement',
    '/diamonds/elegant-engagement-ring-719881',
    '/diamonds/diamond-and-sapphire-engagement-ring-open-offers-719671',
    '/diamonds/cushion-halo-engagement-ring-set-sylvie-719666',
    '/diamonds/200-carat-double-halo-oval-diamond-ring-ivs1-gia-719616',
    '/diamonds/14k-white-gold-engagement-ring-and-wedding-band-set-719441',
    '/diamonds/vera-wang-love-collection-1-ct-tw-oval-diamond-three-stone-engagement-ring-14k-two-tone',
    '/diamonds/video-igi-certified-white-gold-110ct-diamond-solitaire-accent-engagement-ring-round',
    '/diamonds/200-carat-halo-oval-diamond-ring-ivs2-gia-719191',
    '/diamonds/kay-jewelers-halo-princess-cut-engagement-ring-718996',
    '/diamonds/blue-nile-princess-cut-wedding-set-718991',
    '/diamonds/155-h-vvs2-gia-cushion-twist-band-ring-718821',
    '/diamonds/princess-cut-109-blue-topaz-and-green-emeralds-715236',
    '/diamonds/399-cushion-cut-pave-ring-gia-309-i-vvs1-cushion-center-718281',
    '/diamonds/engagement-ring-18k-white-gold-diamond-sapphiressize-4-size-h5-video-available-instagram',
    '/diamonds/551-wedding-set-401-i-vs1-center-cushion-717041',
    '/diamonds/beautiful-matching-bridal-set-716581',
    '/diamonds/wow-gorgeous-cushion-halo-ring-10x10mm-moissanite-center-716251',
    '/diamonds/359-carat-set-gia-3-ct-i-vvs1-cushion-plus-band-716191',
    '/diamonds/brand-new-105mm-old-mine-cut-center-platinum-ring-side-baguettes-716041',
    '/diamonds/520-old-mine-cut-platinum-engagement-ring-new-715986',
    '/diamonds/266-ct-engagement-ring-diamonds-band-715746',
    '/diamonds/3-ring-set-105-mm-4-carat-old-mine-cut-moissanite-center-715561',
    '/diamonds/showstopper-magnificent-387-carat-diamond-and-platinum-vintage-engagement-ring-one-kind',
    '/diamonds/blue-nile-engagement-ring-14k-white-gold-10-carat-total-diamond-weight-center-highly-graded',
    '/diamonds/300-carat-diamond-engagement-ring-250-h-vs2-igi-center-714706',
    '/diamonds/video-new-gia-certified-platinum-134ct-diamond-halo-engagement-ring-631536',
    '/diamonds/182-white-gold-double-halo-122-carat-f-vvs2-round-igi-diamond-center-714506',
    '/diamonds/brand-new-270-halo-engagement-ring-2-ct-i-vs1-gia-center-gorgeous-714486',
    '/diamonds/250-oval-diamond-ring-set-ring-set-150-i-vs1-gia-oval-center-wedding-band-714386',
    '/diamonds/553-platinum-solitaire-diamond-ring-503-vs1-triple-excellent-gia-center-713206',
    '/diamonds/910-carat-natural-princess-cut-diamond-engagement-ring-wedding-ring-set-10k-white-gold',
    '/diamonds/12-tcw-wedding-band-10k-white-gold-713216',
    '/diamonds/177-simon-g-halo-diamond-ring-122-f-vvs2-ex-cut-center-713116',
    '/diamonds/1698000-appraised-2014-106-carat-round-classic-minimalistic-solitaire-mounted-platinum',
    '/diamonds/custom-made-diamondplatinum-ring-5-carat-center-712851',
    '/diamonds/150-h-vvs2-diamond-solitaire-cushion-h-vvs2-712881',
    '/diamonds/princess-cut-engagement-ring-712321',
    '/diamonds/303-carat-3-ring-set-gorgeous-gia-certified-711651',
    '/diamonds/three-ring-set-409-total-carat-weight-309-i-vvs1-gia-center-711636',
    '/diamonds/custom-made-halo-style-2-carat-gia-certified-center-711541',
    '/diamonds/12-carat-round-cut-natural-diamond-engagement-rings-women-band-10kw-solid-gold-711496',
    '/diamonds/2-ct-certified-moissanite-round-solitaire-engagement-ring-14k-yellow-gold-711491',
    '/diamonds/tacori-blue-sapphire-engagement-ring-711451',
    '/diamonds/389-ct-gia-cushion-cut-3-sided-pave-diamond-ring-309-i-vvs1-gia-center-698881',
    '/diamonds/diamond-wedding-band-711061',
    '/diamonds/320-carat-rose-or-white-gold-oval-ring-711031',
    '/diamonds/180-double-halo-style-platinum-ring-h-vvs2-cushiion-center-711011',
    '/diamonds/ritani-diamond-ring-2-ct-gia-certified-i-vs1-round-center-711006',
    '/diamonds/253-halo-cushion-diamond-ring-gia-center-710961',
    '/diamonds/703-triple-excellent-gia-certified-diamond-tiffany-solitaire-set-710836',
    '/diamonds/475-emerald-cut-diamond-eternity-band-710591',
    '/diamonds/330-split-shank-halo-ring-280-carat-ivs2-gia-triple-excellent-center-710301',
    '/diamonds/459-carat-cushion-cut-diamond-ring-3-ct-gia-i-vvs1-center-and-band-710306',
    '/diamonds/video-100ct-gia-certified-platinum-f-vs2-diamond-engagement-ring-bezel-set-halo-bespoke',
    '/diamonds/video-gia-certified-082ct-fancy-light-yellow-platinum-diamond-halo-engagement-ring-710066',
    '/diamonds/300-emerald-cut-gia-ring-split-shank-709606',
    '/diamonds/great-deal-radiant-cut-diamond-133-carat-white-gold-setting-style-709446',
    '/diamonds/wow-great-deal-233-carat-diamond-ring-rare-and-different-709391',
    '/diamonds/classic-and-beautiful-round-diamond-104-carat-certified-platinum-custom-made-709386',
    '/diamonds/15-carat-princess-cut-engagement-ring-pav%C3%A9-set-diamond-band-709201',
    '/diamonds/jacob-co-diamond-ring-171-carat-white-gold-deal-wont-last-709062',
    '/diamonds/14k-yellow-gold-blossoming-vine-engagement-ring-size-4-cushion-gia-084-crt-709011',
    '/diamonds/james-allen-075ct-oval-cut-diamond-engagement-ring-708276',
    '/diamonds/14k-white-gold-2-ct-center-moissanite-and-1-ct-side-natural-diamonds-side-vintage',
    '/diamonds/brand-new-111ctw-round-brilliant-cut-diamond-14k-white-gold-setting-706841',
    '/diamonds/55-carat-round-moissanite-diamond-platinum-solitaire-706776',
    '/diamonds/tacori-platinum-solitaire-engagement-ring-w-1178-ct-ideal-cut-brian-gavin-diamond-matching',
    '/diamonds/252-twist-halo-diamond-engagement-ring-2ct-ivs1gia-center-705421',
    '/diamonds/753-carat-platinum-diamond-ring-set-5-carat-gia-center-vs1-triple-excellent-705251',
    '/diamonds/253-carat-halo-203ct-gia-cushion-cut-center-704951',
    '/diamonds/vintage-filigree-flower-ring-704351',
    '/diamonds/new-250-ajaffe-new-platinum-set-w-band-150-i-vs2-radiant-gia-center-704316',
    '/diamonds/jared-solitaire-round-diamond-engagement-ring-703711',
    '/diamonds/230-ct-ring-pave-200-i-vs1-diamond-gia-certified-703166',
    '/diamonds/elegant-diamond-ringvideo-702901',
    '/diamonds/absolutely-amazing-engagement-setvideo-702896',
    '/diamonds/pear-shaped-diamond-white-gold-engagementband-set-702776',
    '/diamonds/certified-natural-cushion-engagement-ring-702291',
    '/diamonds/151-carat-diamond-ring-classic-and-different-18kt-white-gold-701981',
    '/diamonds/jaffe-180-carat-brand-new-ajaffe-engagement-ring-15-gia-center-701666',
    '/diamonds/deal-day-126-carat-diamond-ring-custom-made-18kt-white-gold-my-loss-your-gain-701531',
    '/diamonds/182-tiffany-style-solitaire-ring-701416',
    '/diamonds/550-platinum-custom-solitaire-moissanite-ring-11mm-old-mine-cut-gorgeous-free-wrap-701311',
    '/diamonds/halo-asscher-cut-diamond-ring-gia-certified-700706',
    '/diamonds/gorgeous-pear-wedding-set-5-cts-700346',
    '/diamonds/080-ctw-round-diamond-engagement-ring-699996',
    '/diamonds/240-ct-i-vs2-gia-center-platinum-ring-and-band-jeff-cooper-699271',
    '/diamonds/round-brilliant-diamond-solitaire-058-diamond-698511',
    '/diamonds/leo-diamond-solitaire-e-color-round-58-carat-brilliant-698506',
    '/diamonds/140-ct-heart-shaped-diamond-ring-698241',
    '/diamonds/313-diamond-engagement-ring-263-j-si1-ex-ex-ex-center-698096',
    '/diamonds/certified-natural-oval-engagement-ringvideo-697691',
    '/diamonds/unbelievable-three-stone-engagement-ringvideo-697696',
    '/diamonds/fantastic-engagement-ring-center-princess-cut-diamondvideo-697701',
    '/diamonds/agi-certified-three-stone-diamond-ring-334tdwvideo-697706',
    '/diamonds/gia-certified-three-stone-diamond-ringvideo-697671',
    '/diamonds/rare-setting-very-different-161-carat-diamond-ring-pear-shape-deal-697366',
    '/diamonds/deal-day-112-carat-diamond-classic-and-plain-setting-style-697391',
    '/diamonds/4-carat-moissanite-cushion-diamond-solitaire-692791',
    '/diamonds/new-ring-jeff-cooper-platinum-set-15-emerald-gia-center-696126',
    '/diamonds/310-oval-diamond-ring-250-center-gia-certified-695646',
    '/diamonds/274-ctw-pear-shaped-engagement-ring-694241',
    '/diamonds/100-carat-ctw-princess-cut-diamond-engagement-rings-set-694176',
    '/diamonds/tiffany-co-round-diamond-engagement-ring-693001',
    '/diamonds/amazing-natural-engagement-ringvideo-691546',
    '/diamonds/elegant-engagement-ringvideo-691226',
    '/diamonds/absolutely-amazing-engagement-ringvideo-691086',
    '/diamonds/200-ct-halo-oval-solitaire-gia-certified-ring-691016',
    '/diamonds/172-new-art-carved-ring-two-tone-rose-gold-center-row-122-f-vvs2-center-691011',
    '/diamonds/25-ct-square-radiant-diamond-ring-radiant-center-new-690891',
    '/diamonds/amazing-diamond-engagement-ringvideo-690831',
    '/diamonds/150-oval-double-halo-ring-gia-certified-689746',
    '/diamonds/beautiful-huge-engagement-ring-video-689531',
    '/diamonds/absolutely-gorgeous-engagement-ringvideo-689451',
    '/diamonds/108-carat-emerald-cut-solitaire-688486',
    '/diamonds/new-fantastic-engagement-ringvideo-688126',
    '/diamonds/white-gold-round-diamond-engagement-ring-and-wedding-band-688051',
    '/diamonds/rose-gold-engagement-ringvideo-687886',
    '/diamonds/very-interesting-engagement-ring-video-687836',
    '/diamonds/absolutely-gorgeous-engagement-ringvideo-687771',
    '/diamonds/new-new-new-engagement-ringvideo-687766',
    '/diamonds/400-carat-eternity-band-687116',
    '/diamonds/beautiful-princess-cut-engagement-ring-686612',
    '/diamonds/170-oval-ivs2-color-gia-certified-center-yellow-twist-rope-band-design-686196',
    '/diamonds/gabriel-co-14kt-rose-gold-and-round-diamond-designer-engagement-ring-686101',
    '/diamonds/kwiat-cushion-diamond-engagement-ring-pave-basket-and-band-platinum-685686',
    '/diamonds/new-certificated-princess-cut-3-stone-diamond-engagement-ring-685211',
    '/diamonds/engagement-ring-240-ct-total-diamond-weight-685236',
    '/diamonds/breathtaking-diamond-ring-agi-certificate-684866',
    '/diamonds/extraordinary-engagement-ring-center-116ct-princess-cut-diamond-video-684876',
    '/diamonds/three-stone-engagement-ring-684886',
    '/diamonds/gorgeous-engagement-ring-256-ct-total-diamond-weight-video-684891',
    '/diamonds/230-cushion-diamond-ring-gia-certifiednew-684931',
    '/diamonds/fantastic-gia-certified-engagement-ring-684731',
    '/diamonds/tiffany-style-cushion-cut-diamond-ring-684726',
    '/diamonds/agi-certified-round-diamond-engagement-ring-226-ct-total-diamond-weight-684721',
    '/diamonds/amazing-natural-marquise-shaped-diamond-engagement-ring-684711',
    '/diamonds/emerald-cut-diamond-engagement-ring-175-ct-total-diamond-weight-684691',
    '/diamonds/fantastic-sapphire-684606',
    '/diamonds/engagement-ring-center-cushion-cut-101ct-diamond-684331',
    '/diamonds/engagement-ring-103ct-total-diamond-weight-684336',
    '/diamonds/gia-certified-engagement-ring-191-ct-total-diamond-weight-684341',
    '/diamonds/gia-certified-engagement-ring-146-ct-total-diamond-weight-684346',
    '/diamonds/engagement-ring-600ct-center-green-emerald-and-two-trapezoid-diamonds-sides-684271',
    '/diamonds/engagement-ring-features-100ct-center-oval-diamond-684281',
    '/diamonds/engagement-ring-center-cushion-cut-103ct-diamond-684291',
    '/diamonds/elegant-engagement-ring-050ct-683406',
    '/diamonds/radiant-cut-yellow-diamond-engagement-ring-wedding-ring-bridal-ring-promise-ring',
    '/diamonds/15-cttw-princess-diamond-3-stone-bridal-engagement-ring-14k-white-gold-682196',
    '/diamonds/12-cttw-2-stone-diamond-hearts-together-bridal-wedding-ring-set-10k-white-gold-682181',
    '/diamonds/2-ctw-double-halo-diamond-engagement-ring-wedding-band-set-10k-white-gold-682191',
    '/diamonds/12-cttw-round-diamond-cindys-dream-bridal-engagement-ring-10k-rose-gold-682186',
    '/diamonds/round-brilliant-diamond-engagement-ring-682016',
    '/diamonds/round-diamond-engagement-ring-430-ct-total-diamond-weight-681016',
    '/diamonds/300-emerald-halo-engagement-ring-25-vvs2-gia-center-680626',
    '/diamonds/deal-day-208-carat-certified-big-look-less-value-680366',
    '/diamonds/gabriel-co-round-diamond-engagement-ring-679546',
    '/diamonds/vintage-platinum-tacori-setting-free-wedding-band-677461',
    '/diamonds/stunning-round-diamond-engagement-ring-set-677316',
    '/diamonds/gia-certified-fantastic-engagement-ring-677311',
    '/diamonds/gia-certified-marquise-diamond-engagement-ring-677306',
    '/diamonds/175-carat-diamonds-18-kt-white-gold-676816',
    '/diamonds/jared-princess-cut-diamond-ring-676771',
    '/diamonds/301-diamond-ring-wedding-set-201-i-vs1-gia-center-diamond-676456',
    '/diamonds/radiant-cut-beautiful-engagement-ring-676061',
    '/diamonds/tacori-260-diamond-ring-180-ct-emerald-gia-center-674566',
    '/diamonds/pear-engagement-ring-674481',
    '/diamonds/170-carat-certified-oval-diamond-white-gold-18-kt-674181',
    '/diamonds/260diamond-engagement-ring-2oo-ivs1-gia-center-673541',
    '/diamonds/gia-certified-300-emerald-cut-diamond-solitaire-25-vvs2-gia-certified-673386',
    '/diamonds/gia-certified-platinum-075ct-cushion-cut-diamond-halo-engagement-ring-597941',
    '/diamonds/210-carat-gia-certified-halo-ring-15ct-i-vs1-center-673241',
    '/diamonds/ritani-diamond-ring-270-carat-triple-exellent-center-gia-cert-672451',
    '/diamonds/122-f-vvs2-diamond-solitaire-white-gold-672221',
    '/diamonds/princess-cut-70-cts-engagement-ring-672096',
    '/diamonds/zales-bridal-set-modern-1-15-ct-tw-diamond-cluster-bridal-set-14k-white-gold-595336',
    '/diamonds/three-stone-round-diamond-engagement-ring-and-wedding-set-671261',
    '/diamonds/princess-cut-diamond-engagement-ring-402-ct-total-diamond-weight-671246',
    '/diamonds/engagement-ring-300-ct-total-diamond-weight-671251',
    '/diamonds/natural-diamond-eternity-band-400tdw-671076',
    '/diamonds/eternity-platinum-band-671086',
    '/diamonds/halo-style-princess-cut-engagement-ring-and-wedding-band-set-670901',
    '/diamonds/three-stone-engagement-set-670726',
    '/diamonds/natural-diamond-engagement-ring-670676',
    '/diamonds/stunning-three-stone-diamond-ring-670506',
    '/diamonds/engagement-rings-set-670511',
    '/diamonds/gia-certified-engagement-ring-670521',
    '/diamonds/amazing-tree-stone-ring-670541',
    '/diamonds/engagement-ring-175-ct-total-diamond-weight-video-670416',
    '/diamonds/rose-gold-diamond-halo-ring-670186',
    '/diamonds/fantastic-sapphire-ring-669026',
    '/diamonds/sale-diamond-rings-set-668736',
    '/diamonds/engagement-rings-set-668741',
    '/diamonds/engagement-ring-256-ct-total-diamond-weight-video-668556',
    '/diamonds/349-platinum-cushion-diamond-ring-309-ivvs1-gia-cushion-certified-center-diamond-668661',
    '/diamonds/fantastic-engagement-ring-gia-certified-664721',
    '/diamonds/diamond-engagement-ring-75ct-two-tapered-baguettes-664886',
    '/diamonds/natural-diamond-engagement-ring-135-ct-total-diamond-weight-663836',
    '/diamonds/white-gold-mens-wedding-band-663751',
    '/diamonds/classic-round-engagement-ring-250-ct-total-diamond-weight-video-663691',
    '/diamonds/natural-diamond-engagement-ring-video-663686',
    '/diamonds/natural-diamond-ring-155-ct-total-diamond-weight-663386',
    '/diamonds/engagement-ring-122-ct-total-diamond-weight-663261',
    '/diamonds/engagement-ring-270-ct-total-diamond-weight-663246',
    '/diamonds/engagement-ring-197-ct-total-diamond-weight-663226',
    '/diamonds/emerald-cut-diamond-engagement-ring-097-ct-total-diamond-weight-663191',
    '/diamonds/pear-shaped-engagement-ring-126-ct-total-diamond-weight-663161',
    '/diamonds/reduced-marquise-diamond-engagement-ring-106-carats-set-yellow-gold-601481',
    '/diamonds/78-8-carat-oval-eternity-band-each-660911',
    '/diamonds/engagement-bridal-set-185-ct-total-diamond-weight-659971',
    '/diamonds/engagement-ring-solitaire-110ct-princess-cut-diamond-659926',
    '/diamonds/big-fantastic-diamond-ring-video-659056',
    '/diamonds/engagement-ring-353-ct-total-diamond-weight-video-659051',
    '/diamonds/engagement-ring-215-ct-total-diamond-weight-video-659036',
    '/diamonds/diamond-halo-egagement-ring-gia-certified-203-cushion-cut-center-658491',
    '/diamonds/410-carat-3-stone-100-natural-old-mine-cut-antique-style-ring-gia-cert-wow-658081',
    '/diamonds/solitaire-engagement-ring-certified-oval-cut-diamond-657971',
    '/diamonds/rose-gold-solitaire-150-i-vs2-gia-center-657811',
    '/diamonds/engagement-ring-657696',
    '/diamonds/white-gold-engagement-ring-center-round-diamond-and-blue-sapphires-sides-618791',
    '/diamonds/wedding-band-657391',
    '/diamonds/eternity-band-657396',
    '/diamonds/round-diamond-solitaire-101-ct-white-gold-setting-cz-ring-travel-601621',
    '/diamonds/engagement-ring-301-ct-total-diamond-weight-637146',
    '/diamonds/engagement-ring-center-fancy-yellow-and-side-white-diamonds-624641',
    '/diamonds/engagement-ring-301-ct-total-diamond-weight-video-641621',
    '/diamonds/platinum-diamond-semi-mount-engagement-wedding-40-ct-side-stones-either-cushion-emerald',
    '/diamonds/custom-14k-white-gold-diamond-engagement-ring-1-carat-42-carat-melee-598411',
    '/diamonds/engagement-ring-312ct-total-diamond-weight-634736',
    '/diamonds/engagement-ring-110ct-total-diamond-weight-634726',
    '/diamonds/engagement-ring-center-100ct-round-diamond-634816',
    '/diamonds/engagement-ring-center-253ct-cushion-cut-diamond-and-side-diamonds-634881',
    '/diamonds/classic-tiffany-style-engagement-ring-635266',
    '/diamonds/engagement-ring-solitaire-108ct-round-cut-diamond-video-635416',
    '/diamonds/engagement-ring-205ct-total-diamond-weight-635011',
    '/diamonds/engagement-ring-solitaire-214ct-round-cut-diamond-platinum-video-626826',
    '/diamonds/classic-three-stone-engagement-ring-center-116ct-round-diamond-620531',
    '/diamonds/classic-white-gold-diamond-engagement-ring-625241',
    '/diamonds/155-ct-radiant-diamond-white-gold-vintage-bezel-set-eternity-engagement-ring-628066',
    '/diamonds/soldcharming-half-way-wedding-diamond-ring-629796',
    '/diamonds/soldplatinum-engagement-ring-solitaire-214ct-round-cut-diamond-video-624661',
    '/diamonds/cocktail-ring-550-ct-total-diamond-weight-video-640411',
    '/diamonds/certified-18k-white-gold-engagement-ring-features-172ct-center-round-diamond-619381',
    '/diamonds/engagement-ring-features-172ct-center-round-diamond-637591',
    '/diamonds/fantastic-diamond-blue-sapphire-ring-637751',
    '/diamonds/certified-18k-white-gold-engagement-ring-solitaire-170ct-princess-cut-diamond-video-644751',
    '/diamonds/gia-certified-diamond-engagement-ring-101-carat-princess-cut-center-gia-certified-347421',
    '/diamonds/incredibly-elegant-101-ct-cushion-cut-diamond-engagement-ring-14kt-white-gold-595661',
    '/diamonds/beautiful-color-stone-cocktail-ring-center-ruby-and-side-diamonds-623381',
    '/diamonds/charming-color-stone-cocktail-ring-center-blue-sapphire-and-side-diamonds-628236',
    '/diamonds/certified14k-white-gold-engagement-ring-center-253ct-cushion-cut-diamond-and-side-diamonds',
    '/diamonds/classic-cocktail-ring-features-280ct-total-white-and-black-diamonds-621386',
    '/diamonds/fantastic-engagement-ring-656711',
    '/diamonds/wedding-set-656566',
    '/diamonds/certified-engagement-ring-video-656576',
    '/diamonds/wedding-set-video-656596',
    '/diamonds/rose-gold-engagement-set-video-656611',
    '/diamonds/19-carat-ring-15-i-vs1-gia-radiant-center-gorgeous-ring-334061',
    '/diamonds/095-ct-princess-diamond-vs2-clarity-plus-2-wedding-bands-additional-075-carats-diamonds',
    '/diamonds/12-ct-round-brilliant-solitaire-diamond-engagement-ring-521126',
    '/diamonds/157ct-round-diamond-modern-engagement-ring-581131',
    '/diamonds/amazing-deal-princess-cut-engagement-ring-566046',
    '/diamonds/womens-fashion-ring-snake-shaped-650191',
    '/diamonds/292-carat-platinum-cushion-cut-solitaire-606961',
    '/diamonds/300-carat-gia-diamond-engagement-ring-25-center-ivs2-round-center-601051',
    '/diamonds/307-oval-diamond-pave-engagement-ring-gia-certified-631296',
    '/diamonds/310-platinum-emerald-diamond-ring-band-250-j-vvs2-gia-center-new-376636',
    '/diamonds/elegant-engagement-ring-center-130ct-princess-cut-diamond-623351',
    '/diamonds/classic-engagement-ring-features-202ct-round-cut-diamond-623616',
    '/diamonds/white-gold-engagement-ring-solitaire-110ct-princess-cut-diamond-623631',
    '/diamonds/charming-18k-white-gold-engagement-ring-features-125-ct-diamonds-628791',
    '/diamonds/18k-white-gold-engagement-ring-fancy-dark-gray-center-diamond-video-632716',
    '/diamonds/charming-120-ct-diamond-ring-632721',
    '/diamonds/14k-white-gold-engagement-ring-center-210ct-round-cut-diamond-619376',
    '/diamonds/white-gold-engagement-ring-solitaire-101ct-princess-cut-diamond-623606',
    '/diamonds/charming-engagement-ring-center-round-108ct-diamond-and-side-diamonds-video-623626',
    '/diamonds/engagement-ring-353-ct-total-diamond-weight-video-640551',
    '/diamonds/fashion-ring-features-center-13-mm-radius-pink-amethyst-video-640596',
    '/diamonds/amazing-097-ct-engagement-ring-632706',
    '/diamonds/delicate-rose-gold-engagement-ring-features-oval-100ct-diamond-video-621746',
    '/diamonds/18k-white-gold-engagement-ring-fancy-greenish-yellow-brown-center-diamond-632711',
    '/diamonds/classic-three-stone-diamond-engagement-ring-diamonds-sides-crafted-18k-yellow-gold-619366',
    '/diamonds/modern-14k-white-gold-engagement-ring-center-100ct-round-diamond-619371',
    '/diamonds/amazing-sapphire-655756',
    '/diamonds/fantastic-sapphire-655771',
    '/diamonds/263-halo-diamond-engagement-ring-yellow-gold-free-wedding-band-632516',
    '/diamonds/charming-yellow-gold-fashion-ring-video-643651',
    '/diamonds/engagement-ring-center-cushion-cut-103ct-diamond-video-648901',
    '/diamonds/engagement-ring-150ct-princess-and-round-cut-diamonds-636371',
    '/diamonds/certified-14k-white-gold-engagement-ring-center-166ct-cushion-cut-diamond-623451',
    '/diamonds/18k-white-gold-engagement-ring-fancy-brownish-yellow-center-diamond-632571',
    '/diamonds/video-classic-white-gold-diamond-band-643656',
    '/diamonds/classic-white-gold-diamond-engagement-ring-623341',
    '/diamonds/certified18k-white-gold-engagement-ring-center-157ct-princess-cut-diamond-623361',
    '/diamonds/engagement-ring-103ct-total-diamond-weight-636401',
    '/diamonds/14k-white-gold-engagement-ring-302ct-natural-princess-cut-diamond-629791',
    '/diamonds/gorgeous-115-ct-diamond-ring-632576',
    '/diamonds/dazzling-three-stone-engagement-ring-features-140ct-total-diamonds-620541',
    '/diamonds/18kt-white-gold-diamond-wedding-band-125ct-diamonds-video-643661',
    '/diamonds/elegant-white-gold-diamond-band-video-643666',
    '/diamonds/extraordinary-18k-white-gold-engagement-ring-center-125ct-round-diamond-621396',
    '/diamonds/fantastic-engagement-ring-center-cushion-cut-101ct-diamond-648906',
    '/diamonds/engagement-ring-center-cushion-cut-101ct-diamond-648911',
    '/diamonds/18k-white-gold-engagement-ring-features-center-100-ct-648916',
    '/diamonds/325-diamond-ring-305-i-vs1-ex-ex-ex-center-igi-606641',
    '/diamonds/63-cushion-diamond-engagement-ring-and-14kw-gold-wedding-band-655296',
    '/diamonds/220-scott-kay-diamond-ring-asscher-cut-ceter-gia-601831',
    '/diamonds/vintage-platinum-tacori-style-ring-style-wedding-band-combo-100ct-moissanite-521811',
    '/diamonds/200-ct-i-vs1-emerald-cut-gia-certified-pave-diamond-mounting-560271',
    '/diamonds/brand-new-603-platinum-diamond-ring-band-save-thousands-560986',
    '/diamonds/amazing-ring-150ct-ivs1center-gia-certified-solitaire-502311',
    '/diamonds/gia-certified-stunning-diamond-engagement-ring-654976',
    '/diamonds/18k-white-gold-engagement-ring-features-center-100-ct-emerald-cut-647956',
    '/diamonds/engagement-ring-600ct-center-green-emerald-and-two-trapezoid-diamonds-sides-648076',
    '/diamonds/170-plat-oval-diamond-solitaire-ring-baguettes-150-i-vs2-gia-center-certified-549386',
    '/diamonds/320ct-oval-pave-diamond-ring-250-j-vvs2-oval-comes-gia-certified-center-575191',
    '/diamonds/10000-retail-2004-jb-star-diamond-encircled-platinum-wedding-band-3565-2021-firm-nearly',
    '/diamonds/delicate-white-gold-engagement-ring-center-122ct-princess-cut-diamond-and-pave-diamonds',
    '/diamonds/engagement-ring-center-round-cut-100ct-diamond-631571',
    '/diamonds/certified-engagement-ring-362-ct-total-diamond-weight-video-643486',
    '/diamonds/engagement-ring-295-ct-total-diamond-weight-video-639366',
    '/diamonds/gia-certified-engagement-ring-285-ct-total-diamond-weight-video-639561',
    '/diamonds/platinum-engagement-diamond-ring-351ct-total-diamonds-618421',
    '/diamonds/yellow-gold-diamond-band-622606',
    '/diamonds/video-engagement-bridal-set-185-ct-total-diamond-weight-639581',
    '/diamonds/video-half-way-18k-white-gold-diamond-band-features-018ct-total-diamonds-639601',
    '/diamonds/14k-white-gold-engagement-ring-122ct-main-round-diamond-618786',
    '/diamonds/elegant-channel-set-diamond-engagement-ring-622591',
    '/diamonds/white-gold-diamond-wedding-band-622621',
    '/diamonds/platinum-engagement-ring-161ct-tdw-635291',
    '/diamonds/magnificent-gia-certified-platinum-wedding-set-216ct-diamonds-gia-certified-618446',
    '/diamonds/white-gold-diamond-wedding-band-622631',
    '/diamonds/platinum-engagement-ring-solitaire-round-cut-diamond-video-643316',
    '/diamonds/engagement-ring-center-cushion-cut-101ct-diamond-video-647876',
    '/diamonds/video-fantastic-engagement-ring-center-cushion-cut-101ct-diamond-647881',
    '/diamonds/amazing-050ct-round-cut-engagement-ring-video-643496',
    '/diamonds/platinum-engagement-three-stone-ring-312ct-total-diamond-weight-gia-certified-618416',
    '/diamonds/half-way-18k-white-gold-diamond-band-features-025ct-total-diamonds-video-639596',
    '/diamonds/beautiful-color-stone-cocktail-ring-center-blue-sapphire-and-side-diamonds-622811',
    '/diamonds/400-set-diamond-ring-set-250i-si1-gia-cushion-center-wedding-band-combo-630941',
    '/diamonds/stunning-gia-certified-080ct-i-vvs1-excellent-cut-round-stone-platinum-014ct-petite-pave',
    '/diamonds/modern-customized-152-carat-18kt-white-gold-amazing-deal-638281',
    '/diamonds/certified-engagement-ring-center-emerald-100ct-diamond-and-side-diamonds-631321',
    '/diamonds/diamond-eternity-band-total-042ct-round-cut-diamonds-627296',
    '/diamonds/diamond-eternity-band-features-320ct-round-diamonds-622286',
    '/diamonds/engagement-ring-center-gia-cushion-217ct-diamond-622291',
    '/diamonds/engagement-ring-center-pear-shape-055ct-diamond-646796',
    '/diamonds/elegant-and-gentle-solitaire-engagement-ring-crafted-white-gold-646831',
    '/diamonds/engagement-ring-center-157ct-princess-cut-diamond-634871',
    '/diamonds/three-stone-platinum-engagement-ring-video-643121',
    '/diamonds/white-gold-engagement-ring-features-030ct-five-round-cut-diamonds-622331',
    '/diamonds/amazing-engagement-ring-527-tdw-video-643341',
    '/diamonds/gorgeous-engagement-ring-334-ct-total-diamond-weight-629781',
    '/diamonds/tiffany-style-engagement-ring-center-round-cut-diamond-621761',
    '/diamonds/classic-101ct-round-engagement-ring-631281',
    '/diamonds/classic-engagement-ring-video-643096',
    '/diamonds/engagement-ring-center-round-cut-diamond-video-635411',
    '/diamonds/super-engagement-ring-video-643091',
    '/diamonds/gorgeous-100ct-round-engagement-ring-631311',
    '/diamonds/white-gold-engagement-ring-solitaire-025ct-round-diamond-622316',
    '/diamonds/engagement-ring-center-cushion-cut-103ct-diamond-647341',
    '/diamonds/classic-elegant-platinum-engagement-ring-053-ct-center-round-diamond-and-050-ct-side',
    '/diamonds/three-stone-yellow-gold-engagement-ring-features-center-050ct-round-diamond-635256',
    '/diamonds/engagement-ring-center-cushion-cut-diamond-635306',
    '/diamonds/classic-engagement-ring-center-natural-round-cut-diamond-video-635396',
    '/diamonds/mens-ring-275-fancy-yellow-moissanite-diamond-tension-set-ring-size-105-510666',
    '/diamonds/charming-engagement-ring-center-cushion-150ct-diamond-and-side-diamonds-626711',
    '/diamonds/amazing-engagement-ring-video-646021',
    '/diamonds/amazing-engagement-ring-center-100ct-radiant-cut-diamond-625426',
    '/diamonds/elegant-engagement-ring-center-119ct-round-cut-diamond-625871',
    '/diamonds/unique-14k-white-gold-diamond-ring-features-060ct-total-diamonds-626991',
    '/diamonds/222-pave-set-matching-band-and-122-f-vvs2-center-604661',
    '/diamonds/15-i-vs1-sq-emasscher-cut-gia-solitaire-601241',
    '/diamonds/201ct-ladies-oval-diamond-engagement-ring-150-i-vs1-gia-center-591691',
    '/diamonds/elegant-engagement-ring-100ct-center-green-emerald-and-two-round-diamonds-sides-video',
    '/diamonds/gorgeous-217ct-princess-engagement-ring-634711',
    '/diamonds/charming-eternity-band-179ct-round-diamonds-and-292ct-blue-sapphires-video-620856',
    '/diamonds/half-way-wedding-diamond-ring-634721',
    '/diamonds/14k-white-gold-engagement-ring-features-100-ct-center-diamond-630671',
    '/diamonds/platinum-eternity-band-features-215ct-total-diamonds-video-620841',
    '/diamonds/radiant-cut-blue-diamond-14k-wg-white-diamonds-gorgeous-641816',
    '/diamonds/unique-half-way-eternity-diamond-ring-060ct-diamonds-620851',
    '/diamonds/engagement-ring-center-100ct-radiant-cut-diamond-625421',
    '/diamonds/tiffany-style-white-gold-engagement-ring-solitaire-025ct-round-diamond-634686',
    '/diamonds/fashion-ring-372-ct-total-diamond-weigh-video-638696',
    '/diamonds/three-stone-engagement-ring-features-205ct-princess-cut-diamonds-630656',
    '/diamonds/platinum-engagement-ring-center-diamond-203ct-d-si2-asscher-cut-630686',
    '/diamonds/270-diamond-solitaire-gorgeous-gia-i-vs1-center-new-ring-296866',
    '/diamonds/gia-certified-amazing-200ct-cushion-cut-engagement-ring-video-638431',
    '/diamonds/250-diamond-engagement-ring-200-i-vs1-center-653516',
    '/diamonds/beautiful-half-way-channel-set-diamond-ring-video-629711',
    '/diamonds/charming-18k-white-gold-cocktail-ring-130ct-natural-diamonds-621401',
    '/diamonds/engagement-ring-center-157ct-princess-cut-diamond-video-642606',
    '/diamonds/classic-engagement-ring-features-six-princess-cut-diamonds-621741',
    '/diamonds/video-engagement-ring-features-105ct-princess-cut-diamonds-642646',
    '/diamonds/engagement-ring-features-100-ct-diamonds-video-642716',
    '/diamonds/classic-three-stone-yellow-gold-engagement-ring-features-center-050ct-round-diamond-621771',
    '/diamonds/classic-three-stone-diamond-engagement-ring-crafted-14k-yellow-goldvideo-629706',
    '/diamonds/beautiful-three-stone-platinum-engagement-ring-101ct-center-round-diamond-621751',
    '/diamonds/stunning-halo-engagement-ring-center-135ct-round-diamond-621756',
    '/diamonds/certified-platinum-engagement-ring-653346',
    '/diamonds/171-engagement-ring-gia-certified-15ct-ivs2-center-600446',
    '/diamonds/brand-new-diamond-engagement-halo-ring-gia-certified-center-stone-586131',
    '/diamonds/engagement-ring-features-150ct-total-diamond-weight-637596',
    '/diamonds/white-gold-engagement-ring-features-119ct-round-cut-diamond-625221',
    '/diamonds/rose-gold-engagement-ring-features-119ct-round-cut-diamond-625231',
    '/diamonds/three-stone-ring-gia-certified-652856',
    '/diamonds/exquisite-103ct-marquise-diamond-engagement-ring-crafted-14k-white-gold-620536',
    '/diamonds/eternity-diamond-band-637736',
    '/diamonds/diamond-eternity-band-total-250ct-round-cut-diamonds-620286',
    '/diamonds/engagement-ring-canter-116ct-round-diamond-641631',
    '/diamonds/charming-eternity-band-400ct-round-diamonds-620301',
    '/diamonds/fantastic-channel-set-blue-sapphires-and-diamond-band-video-629811',
    '/diamonds/classic-diamond-engagement-ring-video-637776',
    '/diamonds/rose-gold-cocktail-diamond-ring-175ct-total-diamond-weight-video-629981',
    '/diamonds/elegant-engagement-ring-center-certified-123ct-round-diamond-620526',
    '/diamonds/white-gold-engagement-ring-features-111ct-princess-cut-diamond-625216',
    '/diamonds/certified-189-ct-diamond-ring-633466',
    '/diamonds/gia-certified-engagement-rings-set-652891',
    '/diamonds/144-carat-fancy-yellow-oval-cut-diamond-engagement-ring-586146',
    '/diamonds/14k-rose-gold-diamond-engagement-ring-652021',
    '/diamonds/emerald-and-diamond-ring-18k-gold-509446',
    '/diamonds/3-stone-radiant-engagement-ring-509941',
    '/diamonds/twin-stone-pear-shape-ring-509441',
    '/diamonds/elegant-white-gold-blue-sapphire-and-diamonds-ring-651381',
    '/diamonds/elegant-engagement-ring-200ct-center-blue-sapphire-and-two-fancy-yellow-pear-shape-diamonds',
    '/diamonds/engagement-ring-old-european-cut-video-ring-644756',
    '/diamonds/amazing-engagement-ring-527-tdw-651091',
    '/diamonds/fashion-diamond-ring-637241',
    '/diamonds/three-stone-engagement-ring-center-234ct-round-diamond-video-628771',
    '/diamonds/engagement-ring-features-100ct-center-oval-diamond-637646',
    '/diamonds/unique-half-way-eternity-diamond-ring-624696',
    '/diamonds/charming-fashion-diamond-ring-637236',
    '/diamonds/extraordinary-engagement-ring-center-116ct-princess-cut-diamond-video-620311',
    '/diamonds/fantastic-090-ct-diamond-ring-633171',
    '/diamonds/gorgeous-100-ct-diamond-ring-633176',
    '/diamonds/certified-platinum-engagement-ring-center-152ct-cushion-cut-diamond-and-side-diamonds',
    '/diamonds/stunning-119-ct-diamond-ring-633196',
    '/diamonds/18k-white-gold-engagement-ring-fancy-dark-orande-brown-center-diamond-633166',
    '/diamonds/18k-white-gold-engagement-ring-fancy-brown-yellow-center-diamond-633181',
    '/diamonds/beautiful-white-gold-engagement-ring-solitaire-100ct-cushion-cut-diamond-623956',
    '/diamonds/beautiful-platinum-engagement-ring-center-202ct-cushion-cut-diamond-624681',
    '/diamonds/platinum-engagement-ring-center-301ct-cushion-cut-fancy-yellow-diamond-video-650846',
    '/diamonds/fantastic-engagement-ring-video-640861',
    '/diamonds/gorgeous-engagement-ring-256-ct-total-diamond-weight-video-636886',
    '/diamonds/gorgeous-white-gold-diamond-engagement-ring-153ct-tdw-video-640941',
    '/diamonds/14k-white-gold-engagement-ring-165-ct-total-diamond-weight-618921',
    '/diamonds/platinum-engagement-ring-five-round-cut-diamonds-206ct-total-diamond-weight-618796',
    '/diamonds/platinum-engagement-three-stone-ring-312ct-total-diamonds-gia-certified-618441',
    '/diamonds/14k-yellow-gold-classic-engagement-ring-center-068ct-round-diamond-618936',
    '/diamonds/beautiful-half-way-wedding-diamond-ring-627371',
    '/diamonds/three-stone-engagement-ring-100ct-center-round-diamond-629071',
    '/diamonds/engagement-ring-center-116ct-princess-cut-diamond-video-640961',
    '/diamonds/classic-engagement-ring-center-gia-cushion-217ct-diamond-619991',
    '/diamonds/diamond-eternity-wedding-band-total-100ct-round-cut-diamonds-627326',
    '/diamonds/delicate-rose-gold-engagement-ring-features-075ct-total-diamonds-622296',
    '/diamonds/certified-platinum-engagement-ring-415-ct-total-diamond-weight-video-640811',
    '/diamonds/video-certified-white-gold-engagement-ring-400-ct-total-diamond-weight-640856',
    '/diamonds/solitaire-engagement-ring-certified-101ct-princess-cut-diamond-619986',
    '/diamonds/fantastic-diamond-wedding-band-total-057ct-round-cut-diamonds-628921',
    '/diamonds/platinum-engagement-ring-features-103-ct-diamonds-618931',
    '/diamonds/charming-diamond-eternity-band-features-500ct-round-diamonds-video-629086',
    '/diamonds/modern-engagement-ring-150ct-total-diamond-weight-crafted-white-gold-618781',
    '/diamonds/fantasticagement-ring-center-301ct-cushion-cut-fancy-yellow-diamond-619796',
    '/diamonds/beautiful-diamond-eternity-band-features-500ct-round-diamonds-video-629076',
    '/diamonds/classic-half-way-wedding-diamond-band-628916',
    '/diamonds/yellow-gold-engagement-ring-features-118ct-total-diamond-weight-618941',
    '/diamonds/classic-elegant-platinum-engagement-ring-center-105-radiant-fancy-yellow-diamond-619651',
    '/diamonds/solitaire-rose-gold-engagement-ring-172ct-cushion-diamond-622311',
    '/diamonds/18k-white-gold-engagement-ring-solitaire-100ct-round-cut-diamond-631256',
    '/diamonds/diamond-eternity-band-features-400ct-emerald-diamonds-636811',
    '/diamonds/243-scott-kay-engagement-ring-203-ct-gia-cushion-enter-636856',
    '/diamonds/tiffany-co-d-vs1-platinum-round-engagement-ring-solitaire-502166',
    '/diamonds/classic-engagement-ring-cushion-cut-certified-150-carat-great-deal-637826',
    '/diamonds/round-brilliant-cut-engagement-ring-114ct-center-beautiful-598111',
    '/diamonds/custom-engagement-ring-round-diamond-120-carat-certified-641896',
    '/diamonds/152ct-engagement-ring-620196',
    '/diamonds/stunning-custom-251-tcw-gia-radiant-engagement-ring-wedding-band-630266',
    '/diamonds/stunning-14k-yellow-gold-engagement-diamond-ring-beautiful-gia-certified-051ct-centre',
    '/diamonds/069-carat-round-diamond-solitaire-engagement-ring-610826',
    '/diamonds/striking-2-carat-asscher-cut-engagement-ring-562791',
    '/diamonds/110-ct-total-weight-princess-cut-diamond-engagement-ring-562816',
    '/diamonds/130-ct-emerald-cut-center-diamond-engagement-ring-18kt-white-gold-562806',
    '/diamonds/engagement-and-wedding-band-set-517976',
    '/diamonds/diamond-encrusted-two-heart-engagement-ring-490681',
    '/diamonds/stylish-bezel-set-center-diamond-set-platinum-band-artisticaly-carved-design-both-sides-080',
    '/diamonds/halo-ring-features-exclusive-three-stone-design-round-cut-diamonds-platinum-setting100-ct',
    '/diamonds/steal-artisan-made-heirloom-6-ct-engagement-ring-306956']

i = 0


textfile = open(write_file, "a")


for url in href_collect:
    
    target_url = "https://www.idonowidont.com" + url
    #Opens the webpage, reads it into a container, then closes the client
    uClient = urlopen(target_url)
    page_html = uClient.read()
    uClient.close()

    soup_html = bs(page_html, "html.parser")

    try:
        #gets price
        container_price = soup_html.find("span", {"class":"product-price"})
        price = container_price.get_text()
    except:
        pass

    try:
        #gets carat
        container_carat = soup_html.find("li", {"class":"field_carat_weight"})
        carat = container_carat.div.div.get_text()
    except:
        pass
    
    try:
        #gets clarity
        container_clarity = soup_html.find("li", {"class":"field_clarity"})
        clarity = container_clarity.div.div.get_text()
    except:
        pass

    try:
        #gets shape
        container_shape = soup_html.find("li", {"class":"field_shape"})
        shape = container_shape.div.div.get_text()
    except:
        pass

    try:
        #gets color
        container_color = soup_html.find("li", {"class":"field_color"})
        color = container_color.div.div.get_text()
    except:
        pass

    # values = []
    # values = [target_url, price, carat, clarity, shape, color]
    values = target_url + "," + price + "," + carat + "," + clarity + "," + shape + "," + color


    textfile = open(write_file, "a")
    textfile.write(values + "\n")
    textfile.close()

    

    # rings.append(values)

# print(rings)

#Build logic to check if new ring is already in master list
#If new ring is in master list, ignore ring
#if new ring is not in master list, mine data and append to masterlist

import os
import bs4
import urllib

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as bs
from pprint import pprint


container_posting_url = []
#gets directory of current working file
dir_path = os.path.dirname(os.path.realpath(__file__))

base_url = "https://www.idonowidont.com/marketplace/men's-watches"
master_list = dir_path + "\master_list_watches.txt"
data_list = dir_path + "\data_list_watches.txt"

print(master_list, data_list)

#Find the last page to loop through
uClient = urlopen(base_url)
page_html = uClient.read()
uClient.close()
soup_html = bs(page_html, "html.parser")
last_page_url = soup_html.find("li", {"class":"pager__item pager__item--last"}).a["href"] 

# not sure why last page is off by -1, so we add 1
last_page = int(last_page_url[-2:]) + 1


# Loop through list of pages to gather all posting url
# and add url to our master_list if it's not in the file
for i in range(0, last_page + 1):
    if i == 0:
        my_url = base_url
    else:
        my_url = base_url + "?page=" + str(i)
    
    print(my_url)

    #Opens the webpage, reads it into a container, then closes the client
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()

    #Uses soup to parse down to href to get weblink
    soup_html = bs(page_html, "html.parser")
    container_posting = soup_html.findAll("div", {"class":"ds-1col"})

    for posts in container_posting:
        post_url = posts.div.a["href"]
        with open(master_list, "r+") as file:
            if post_url in file.read():
                pass
            else:
                file.write(post_url + "\n")


# Read master_list and check if link is valid
# if valid, continue with data mine
# if invalid, remove from master_list

with open(master_list) as f:
    master_list_urls = [line.rstrip() for line in f]
    print(master_list_urls)

with open(data_list) as g:
    data_list_urls = [line.rstrip() for line in g]
    print(data_list_urls)

for url in master_list_urls:
    target_url = "https://www.idonowidont.com" + url
    print(target_url)

    with urlopen(target_url) as client:
        if client.status != 200 and target_url not in data_list_urls:
            pass
        else:
            page_html = client.read()

    soup_html = bs(page_html, "html.parser")

    try:
        #gets price
        container_price = soup_html.find("span", {"class":"product-price"})
        price = container_price.get_text()
    except:
        pass

    try:
        #gets carat
        container_carat = soup_html.find("li", {"class":"field_carat_weight"})
        carat = container_carat.div.div.get_text()
    except:
        pass
    
    try:
        #gets clarity
        container_clarity = soup_html.find("li", {"class":"field_clarity"})
        clarity = container_clarity.div.div.get_text()
    except:
        pass

    try:
        #gets shape
        container_shape = soup_html.find("li", {"class":"field_shape"})
        shape = container_shape.div.div.get_text()
    except:
        pass

    try:
        #gets color
        container_color = soup_html.find("li", {"class":"field_color"})
        color = container_color.div.div.get_text()
    except:
        pass

    # values = []
    # values = [target_url, price, carat, clarity, shape, color]
    values = target_url + "|" + price + "|" + carat + "|" + clarity + "|" + shape + "|" + color

    textfile = open(data_list, "a")
    textfile.write(values + "\n")
    textfile.close()

