#!/usr/bin/env python3
"""Recounts the shares in sites.csv from posts.csv, and the posts with each trace of a Russian original. Python 3, standard library only.
Run: python3 count.py"""
import csv
from collections import defaultdict

posts = list(csv.DictReader(open("posts.csv", encoding="utf-8")))
sites = {r["site"]: r for r in csv.DictReader(open("sites.csv", encoding="utf-8"))}
n = defaultdict(lambda: defaultdict(int))
for p in posts:
    s = n[p["site"]]
    s["posts"] += 1
    s["russian"] += bool(p["russian_outlets_named"] or p["russian_signoff_lines"])
    s["state_terms"] += bool(p["russian_state_terms"])
    s["chinese"] += bool(p["chinese_state_media_named"])
    s["iranian"] += bool(p["iranian_state_media_named"])

columns = [("russian", "share_naming_russian_source"), ("state_terms", "share_with_russian_state_terms"),
           ("chinese", "share_naming_chinese_state_media"), ("iranian", "share_naming_iranian_state_media")]
same = True
print(f"{'site':20} {'posts':>5}  Russian  state terms  Chinese  Iranian")
for site, s in sorted(n.items()):
    shares = [f"{100 * s[k] / s['posts']:.1f}%" for k, _ in columns]
    same &= all(sh == sites[site][col] for sh, (_, col) in zip(shares, columns))
    print(f"{site:20} {s['posts']:5}  {shares[0]:>7}  {shares[1]:>11}  {shares[2]:>7}  {shares[3]:>7}")
print(f"{len(posts)} posts; the shares {'match' if same else 'do NOT match'} sites.csv")

traces = defaultdict(int)
for p in posts:
    for col in ("russian_signoff_lines", "russian_state_terms", "russian_name_forms"):
        for v in filter(None, p[col].split("; ")):
            traces[v] += 1
print("\nPosts with each trace of a Russian original:")
for k, v in sorted(traces.items(), key=lambda kv: -kv[1]):
    print(f"  {k:28} {v:5}")
