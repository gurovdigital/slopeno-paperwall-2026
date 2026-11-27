# Narrative laundering: 14 fake news sites in Spanish whose posts name Russian media

Data by Dosimeter, an independent research group from Berlin: https://dosimeteraudit.org

Dosimeter studied 14 websites in Spanish that look like local news sites from Spain, Colombia, Argentina, Mexico and Chile.

All 14 belong to Paperwall, a network that [Citizen Lab](https://citizenlab.ca/research/paperwall-chinese-websites-posing-as-local-news-outlets-with-pro-beijing-content/) linked to the Chinese PR firm Haimai in February 2024.

In March 2026, the [European External Action Service (EEAS)](https://www.eeas.europa.eu/eeas/4th-eeas-report-foreign-information-manipulation-and-interference-threats_en) reported that the network now fills its sites with translations of Russian media, including state-controlled media.

On 21 November 2026, eight days before Spain's general election, Dosimeter read the newest posts of the 14 sites, 20,996 posts in total.

| Site | Styled as | Posts in total | First post | Posts with a Russian source |
|---|---|---|---|---|
| cordovapress.org | Córdoba, Spain | 18,950 | 2021-01-15 | 19.2% |
| guellherald.com | Barcelona, Spain | 15,213 | 2022-12-30 | 21.8% |
| sevillatimes.com | Seville, Spain | 22,222 | 2021-01-14 | 16.9% |
| tarragonapost.com | Tarragona, Spain | 22,172 | 2022-12-30 | 16.8% |
| andregaceta.com | Colombia | 18,447 | 2023-04-17 | 25.7% |
| doloreshoy.co | Dolores, Colombia | 13,447 | 2023-03-28 | 14.2% |
| martapost.com | Santa Marta, Colombia | 16,757 | 2023-04-07 | 15.5% |
| laplatapost.com | La Plata, Argentina | 19,303 | 2023-04-10 | 13.3% |
| lguazu.com | Iguazú, Argentina | 19,267 | 2023-04-14 | 13.1% |
| lujanexpresar.com | Luján, Argentina | 15,173 | 2023-04-10 | 18.4% |
| olmecpress.com | Mexico | 18,098 | 2023-03-28 | 18.4% |
| teotihuacaneco.com | Teotihuacán, Mexico | 14,029 | 2023-04-13 | 18.2% |
| xochimilcolife.com | Xochimilco, Mexico | 14,178 | 2023-03-28 | 17.2% |
| sanrafaelscoop.com | San Rafael, Chile | 13,128 | 2023-04-28 | 19.6% |

## Findings

- Between 13.1% and 25.7% of a site's posts have a Russian source
- Some posts keep the sign-off line of the Russian outlets MK (Moskovsky Komsomolets) or Rambler, which asks readers to follow them on VKontakte, Odnoklassniki or the Russian messenger MAX
- Some posts quote Chinese state media such as Xinhua, CGTN (China Global Television Network) and CCTV (China Central Television)
- Some posts quote Iranian state agencies such as Fars and Tasnim

## Recount

The script `count.py` recounts the shares in `sites.csv` from `posts.csv`, and the number of posts with each trace of a Russian original that the study names. It needs only Python 3 with its standard library.

```
python3 count.py
```

## Files

- `sites.csv`: one row per site, with:
  - the city and country the site presents itself as (two sites give only a country)
  - the number of posts and the date of the first post
  - the period of the posts that were read
  - the shares of posts that name Russian, Chinese and Iranian sources
  - a copy of the home page in the Wayback Machine of the Internet Archive
- `posts.csv`: the 20,996 posts: site, date, address, section, the title in Spanish, the Russian, Chinese and Iranian sources named in the post and the traces of Russian originals, without the texts of the posts
- `articles.csv`: 18 example posts with an English translation of the title, what is notable in each and a copy in the Wayback Machine
- `count.py`: the script that recounts the shares

## Method

The 14 sites run on WordPress, and their lists of posts are open without an account. Dosimeter read about 1,500 of the newest posts per site.

The sites publish at different rates, so the posts that were read cover from about two months to about a year, as the columns `checked_from` and `checked_to` show, so the shares describe the newest posts of each site and do not rank the sites.

A post has a Russian source when its title or text names one of these outlets or state bodies, in the Latin spelling of the translations:

- news agencies: TASS, RIA Novosti, Interfax, Regnum
- newspapers and news sites: Izvestia, Kommersant, Rossiyskaya Gazeta, Komsomolskaya Pravda, MK (Moskovsky Komsomolets), Argumenty i Fakty, RBC (RosBusinessConsulting), Lenta.ru, Gazeta.ru, Rambler, URA.RU, NEWS.ru, Pravda.ru, Life
- TV channels and state media abroad: Russia Today, Sputnik, MIR 24, REN TV, Zvezda, Tsargrad
- Telegram channels: SHOT, Mash, Baza
- state bodies: the Russian Ministry of Defence

In the posts, "SHOT", "Mash" and "Baza" stand as names of Russian Telegram channels ("el canal de Telegram Mash"), and "Life" is counted only before a verb such as "escribió" or "informa".

A post also has a Russian source when it keeps the sign-off line of MK, Rambler or RBC, or a link line to VKontakte. The line of Rambler reads "suscríbase a Rambler en las redes sociales: VKontakte, Classmates", and the line of MK invites readers to its channel in the messenger MAX.

The same rule finds Chinese state media (Xinhua, CGTN, CCTV, China Daily, Global Times, People's Daily, CICG, China News Service and China Radio International) and Iranian state media (IRNA, the Islamic Republic News Agency; Tasnim; Fars; Mehr; Press TV; IRIB, Islamic Republic of Iran Broadcasting; HispanTV; Pars Today and Tehran Times).

The column `russian_state_terms` marks posts with Russian state terms as the machine translation writes them: "SVO" (the Russian abbreviation for "special military operation"), its mistranslation "Distrito Militar del Norte" and the phrase "Kyiv regime" in its Spanish form. The column `russian_name_forms` marks posts that write the name of Ukraine's president in its Russian form, "Vladimir Zelensky".

## Licence

The script is licensed under MIT OR EUPL-1.2 ([LICENSE-MIT](LICENSE-MIT), [LICENSE](LICENSE)), and Dosimeter's own data and documentation under CC BY 4.0 ([LICENSE-DATA.md](LICENSE-DATA.md)). The titles of the posts belong to the sites and are quoted from public pages for research.

The data can be cited as Dosimeter (2026), Narrative laundering: 14 fake news sites in Spanish whose posts name Russian media, data package.

Contact: contact@dosimeteraudit.org
