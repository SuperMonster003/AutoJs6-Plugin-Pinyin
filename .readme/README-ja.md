<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>中国語ピンイン変換用の Pinyin プラグイン</p>

  <p>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SuperMonster003/AutoJs6-Plugin-Pinyin?label=Release"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/SuperMonster003/AutoJs6-Plugin-Pinyin?color=A24232&label=Issues"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/SuperMonster003/AutoJs6-Plugin-Pinyin?color=534BAE&label=License"/></a>
  </p>
</div>

******

### 言語 (Languages)

******

現在の README.md は次の言語に対応しています:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- 日本語 [ja] # 現在
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- [العربية [ar]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ar.md)

******

### 概要

******

Pinyin プラグイン (Pinyin Plugin) は AutoJs6 にオフラインの中国語ピンイン変換機能を提供します. インストール後, スクリプトはグローバルオブジェクト `pinyin` を通じて中国語テキストをさまざまなスタイルのピンインへ変換でき, 多音字の候補, フレーズ辞書, Jieba 単語分割, 姓氏モードをサポートし, ソート, 検索, 頭文字インデックス, 発音注記などの自動化シナリオに適しています.

プラグインは独立してインストールされる APK として自身のプロセスで動作し, AutoJs6 がプラグイン機構により自動検出して AIDL で通信します. 単漢字, フレーズ, 単語分割の辞書はすべて内蔵されており (インストールパッケージは約 6 MB), 変換は完全に端末内で完結し, ネットワークを必要としません. AutoJs6 v6.8.0 以降, ホストの `pinyin` モジュールは本プラグインが実装を提供します. API 設計は JavaScript エコシステムで広く使われている [pinyin](https://github.com/hotoo/pinyin) ライブラリに合わせているため, 同ライブラリに慣れたユーザーならすぐに使い始められます.

本プラグインと [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) は互いに姉妹プラグインです: 本プラグインは辞書が充実し, 多音字と単語分割をサポートするため, 読みの正確さを重視するシナリオに適しています; Pinyin4j は定番の Java ライブラリ pinyin4j をベースにし, サイズはわずか約 0.3 MB で, 軽量な文字単位の変換に適しています. 両者は同時にインストールでき, 詳しくは下の `姉妹プラグインの比較` を参照してください.

******

### 機能ハイライト

******

- すぐに使える: インストール後は AutoJs6 が自動検出し, ホストの再起動は不要で, スクリプトからグローバルオブジェクト `pinyin` を直接使用できます.
- 充実した辞書: 単漢字, フレーズ, 単語分割の 3 つの辞書と HMM モデルを内蔵し, 完全オフラインで, ネットワークリクエストを一切発行しません.
- 多音字サポート: `heteronym` オプションは各文字の全読み候補を返し, フレーズ辞書は常用の読みを自動的に選択します.
- Jieba 単語分割: `segment` オプションで単語分割を有効にすると, フレーズ単位で多音字の曖昧さを解消し, 文全体の読み付与の精度を高めます.
- 6 種類のピンインスタイル: 声調記号, 数字声調, 韻母直後の数字, 声調なし, 声母のみ, 頭文字のみをそろえ, ソート/検索/発音注記などのシナリオをカバーします.
- 固有名モード: `SURNAME` は姓氏専用の読みを優先し, `PLACE_NAME` は出典を追跡できる精選地名コーパスを適用してから通常変換へフォールバックします.
- 組み合わせ可能な結果: `convert` が返す 2 次元候補配列には `compact()` メソッドが付属し, 全読み組み合わせをワンステップで展開できます.
- 多言語対応: プラグイン情報, 使用説明, README, 更新履歴が 10 言語で提供されます.

******

### 使用方法

******

1. AutoJs6 を内部ビルド 3923 (6.7.1 Alpha4) 以上に更新します; v6.8.0 以降ピンイン機能は完全にプラグインが担うため, 最新バージョンの利用を推奨します.
2. [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) ページからプラグイン APK をダウンロードして AutoJs6 が動作する端末にインストールするか, AutoJs6 のプラグインセンターから直接オンラインでインストールします.
3. AutoJs6 のプラグインセンターを開き, `Pinyin` プラグインが認識され, 許可が完了して有効になっていることを確認します.
4. スクリプトからグローバルオブジェクト `pinyin` を直接呼び出します. 下の `クイックスタート` の例を参考にしてください; 先に `セルフチェック` を実行してプラグインの動作を確認することもできます.

> プラグインは汎用インストールパッケージを 1 つだけ提供し (純粋な JVM 実装で CPU アーキテクチャを区別しません), Android 7.0 (API 24) 以上の端末をサポートします. プラグインには独立した画面がなく, インストール後もホーム画面にアイコンを作成せず, AutoJs6 が一括して検出と管理を行います.

******

### クイックスタート

******

基本の変換: `convert` は 2 次元候補配列を, `simple` はコンパクトな文字列を返します:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

多音字: `heteronym` オプションは全読み候補を返し, `compact()` は読みの組み合わせに展開します:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

単語分割による曖昧さの解消, 姓氏モードと地名モード:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### ピンインスタイル

******

`style` オプションはピンインの出力スタイルを制御します. 以下では "中" (zhōng) を例にします:

| スタイル | 出力 | 説明 |
|---|---|---|
| `TONE` | `zhōng` | 韻母に声調記号を付与 (既定) |
| `TONE2` | `zhong1` | 声調を数字 0-4 として音節末尾に付加 |
| `TO3NE` | `zho1ng` | 声調数字を韻母の直後に配置 |
| `NORMAL` | `zhong` | 声調なし |
| `INITIALS` | `zh` | 声母のみを返す (零声母の字は空文字列) |
| `FIRST_LETTER` | `z` | ピンインの頭文字のみを返す |

`style` の値は大文字小文字を区別せず, 文字列 (例: `"TONE2"`) でも定数 (例: `pinyin.STYLE_TONE2`) でも指定できます.

******

### オプション

******

`pinyin.convert(text, options)` は次のオプションをサポートします:

| オプション | 既定値 | 説明 |
|---|---|---|
| `style` | `TONE` | ピンインスタイル, 上の `ピンインスタイル` を参照 |
| `mode` | `NORMAL` | 変換モード: `NORMAL` は通常テキスト, `SURNAME` は姓氏読み, `PLACE_NAME` は精選された地名読み |
| `segment` | `false` | Jieba 単語分割を有効化し, フレーズ辞書で多音字の曖昧さを解消 |
| `heteronym` | `false` | 第一候補だけでなく各文字の全読み候補を返す |
| `group` | `false` | 分割で得たフレーズ単位にピンイン候補を結合 (`segment` と併用) |
| `customDictionary` | `{}` | 現在の呼び出しだけに適用する漢字読みの上書きです. 形式は `{ 語句: [[声調付き候補], ...] }` で最長一致が優先され, 永続化されません. 対応する AutoJs6 ホストとプラグインが必要です |

モードには定数 (例: `pinyin.MODE_PLACE_NAME`) も指定できます. `PLACE_NAME` は小規模な手動確認済みコーパスを最長一致で検索し, 未収録のテキストは `NORMAL` にフォールバックします. 全国地名の完全な台帳ではありません; [コーパスと出典](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md) を参照してください.

******

### スクリプト API

******

グローバルオブジェクト `pinyin` は次のメソッドを提供します (`pinyin(text, options)` の直接呼び出しは `pinyin.convert` と等価です):

```text
pinyin(text, options?)                   -> string[][]
pinyin.convert(text, options?)           -> string[][]
pinyin.simple(text, numeric?, segment?)  -> string
pinyin.compare(textA, textB)             -> number
pinyin.compact(matrix)                   -> string[][]
pinyin.fromCodePoint(codePoint)          -> string | null
pinyin.fromPhrase(phrase)                -> string[][]
pinyin.STYLE_* / pinyin.MODE_*           -> constants
```

- `convert` は 2 次元配列を返します: 漢字またはフレーズ内の各文字スロットが 1 行を占め, 行内はその読み候補です; 未収録文字と非中国語文字はそのまま 1 行を占めます. 返される配列には `compact()` メソッドが付属し, 全読み組み合わせに展開できます.
- `simple` はコンパクトな文字列を返します: 各文字の第一候補の読みをそのまま連結します; 第 2 引数が `true` のときは数字声調 (TONE2 スタイル) で出力し, それ以外は声調なしです; 第 3 引数が `true` のときは単語分割を有効にします.
- `fromCodePoint` は単一コードポイントの辞書上の元の読みレコード (カンマ区切りの声調付き候補) を照会し, 未収録の場合は `null` を返します.
- `fromPhrase` はフレーズ辞書を照会し, そのフレーズの各文字スロットの読み候補を返します; 未収録の場合は空配列を返します.
- すべてのメソッドは同期的に返ります; 初回呼び出しでは内蔵辞書の初期化が必要なため, わずかに時間がかかることがあります.

#### Node.js

Node.js ランタイムでは公開 `autojs6:bridge` facade から同じ provider を呼び出し, `pinyin` capability を明示的に宣言します:

```javascript
const { callAutoJs } = require("autojs6:bridge");

(async () => {
  const result = await callAutoJs(
    "pinyin",
    "convert",
    ["中心", { style: "TONE2" }],
    { permissions: ["pinyin"] },
  );
  console.log(result); // [["zhong1"], ["xin1"]]
})();
```

******

### セルフチェック

******

プラグインをインストールして有効化した後, 次の 1 行スクリプトを実行します:

```javascript
console.log(pinyin.simple("拼音"));
```

`pinyin` と出力されればプラグインは正常に動作しています.

******

### よくある質問

******

#### プラグインが有効になったことをどう確認できますか?

AutoJs6 のプラグインセンターを開き, `Pinyin` プラグインが表示され有効になっていればホストに認識されています; さらに上の `セルフチェック` スクリプトを実行し, `pinyin` と出力されれば正常に機能しています.

#### スクリプトでプラグインが見つからない, または `pinyin` が利用できないというエラーが出ます?

AutoJs6 の内部ビルドが 3923 以上であること, そしてプラグインセンターでプラグインのインストール, 許可, 有効化が完了していることを確認してください. AutoJs6 v6.8.0 以降, ホストはピンイン実装を内蔵しなくなり, ピンイン機能は完全に本プラグインが担います.

#### アプリ一覧やホーム画面にプラグインのアイコンがないのはなぜですか?

正常な動作です. プラグインには独立した画面がなく, ホーム画面にランチャーアイコンも作成しません. インストール後は AutoJs6 がバックグラウンドで自動的に検出して呼び出し, すべての操作は AutoJs6 内で完結します.

#### 多音字の読みが期待どおりになりません?

既定では単漢字の第一候補の読みで変換します. `segment` オプションを有効にしてフレーズ辞書と単語分割による曖昧さの解消を利用することをお勧めします (例: `pinyin.simple(text, false, true)`); 全候補が必要な場合は `heteronym` オプションを使用してください. よく使う語の読みがそれでも正しくない場合は, [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) からのフィードバックで辞書の改善にご協力ください.

#### 姉妹プラグイン Pinyin4j とどちらを選べばよいですか?

多音字, 単語分割, フレーズ, 姓氏の読みが必要な場合は本プラグインを, 軽量な文字単位の変換だけで十分でインストールサイズが気になる場合は [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) を選んでください. 両者は競合せず同時にインストールできます. 詳しくは下の `姉妹プラグインの比較` を参照してください.

#### プラグインはネットワークに接続したり機密性の高い権限を要求したりしますか?

いいえ. すべての辞書はインストールパッケージに内蔵され, 変換は端末内で完結します; プラグインのマニフェストは AutoJs6 との通信に必要なプラグイン権限のみを宣言し, ネットワークやストレージなどの機密性の高いシステム権限は一切要求しません.

#### インストールパッケージが約 6 MB あるのはなぜですか?

インストールパッケージには単漢字辞書, フレーズ辞書, 単語分割用の語彙, HMM モデルの 4 つのデータを内蔵しており, その分完全オフラインとより高い読み付与の精度を実現しています. サイズを重視する場合は, 約 0.3 MB の姉妹プラグイン [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) をご検討ください.

#### `customDictionary` または Node.js のピンイン呼び出しが拒否されるのはなぜですか?

これらの経路には対応する AutoJs6 と Pinyin プラグインが必要です. Node.js 呼び出しでは `permissions: ["pinyin"]` を宣言してください. カスタム辞書は 1 回の呼び出しだけに適用され, 文書化されたエントリ数, 候補数, 組み合わせ数, 64 KiB の上限を守る必要があります.

******

### 権限とセキュリティ

******

プラグインは設計上, データ面と権限面を可能な限り狭めています:

- 最小権限: プラグインのマニフェストは AutoJs6 プラグイン権限 (`org.autojs.permission.PLUGIN`) のみを宣言し, ネットワーク, ストレージ, カメラなどの機密性の高いシステム権限を要求しません.
- ローカル変換: 変換対象のテキストは Binder 経由で端末内のみを移動し, 辞書はすべて内蔵で, 全過程がオフラインのため, データが端末の外に出ることはありません.
- 署名と許可: AutoJs6 はプラグインの署名を検証し, プラグインはプラグインセンターで許可されて有効化された後にのみスクリプトから呼び出せます; サービスとウェイクエントリはいずれもプラグイン権限で保護され, サードパーティアプリから直接呼び出せません.
- オープンソースで監査可能: プラグインコード, 辞書のパッケージング, ドキュメント生成パイプラインはすべてオープンソースです.

プラグインのインストールパッケージは公式の [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) ページまたは AutoJs6 のプラグインセンターからのみ入手してください; 出所不明のパッケージは, 名前とバージョン番号が同じでも改ざんされている可能性があります.

******

### 姉妹プラグインの比較

******

AutoJs6 は公式に 2 つのピンインプラグインを提供しており, それぞれ重点が異なり, 同時にインストールできます:

| 比較項目 | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| 内部実装 | 内蔵辞書 + Jieba 単語分割 | 定番の Java ライブラリ `pinyin4j` |
| グローバルオブジェクト | `pinyin` | `pinyin4j` |
| 多音字 | 対応, 全候補を返却可能 | 非対応, 常に最初の読み |
| 単語分割とフレーズ | 対応 (フレーズ辞書 + Jieba) | 非対応, 文字単位の変換 |
| 姓氏モード | 対応 | 非対応 |
| 出力形式 | 2 次元候補配列 (`compact()` で組み合わせ可) またはコンパクトな文字列 | 文字列, 区切り文字を設定可能 |
| スタイルと形式 | 6 種類のピンインスタイル | 3 種類の声調形式 + 大文字小文字 + `ü` の表記方法 |
| インストールサイズ | 約 6 MB (内蔵辞書) | 約 0.3 MB |
| 適した用途 | 読みの正確さ優先: 多音字, フレーズ, 人名 | サイズと簡潔さ優先: 手軽な文字単位の変換 |

2 つのプラグインは互いに依存も競合もしません; 同時にインストールすれば, スクリプトから必要に応じて `pinyin` と `pinyin4j` をそれぞれ呼び出せます. Pinyin4j プラグインの詳細は [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) を参照してください.

******

### プラグインインターフェース

******

以下の情報は AutoJs6 ホストとプラグイン開発者向けです. ホストはこれらの識別子でプラグインを検出し, 機能ネゴシエーションを行います:

```text
application id: io.github.supermonster003.autojs6.plugin.pinyin
plugin id: pinyin
engine: pinyin
variant: default
discovery action: org.autojs.plugin.PINYIN
discovery category: pinyin
wake action: org.autojs.plugin.action.WAKE
binder interface: IPinyinPlugin
binder methods: getInfo / convert / simple / fromCodePoint / fromPhrase
minimum host build: 3923
native library: none (pure JVM, all ABIs)
```

`PinyinPluginService` は `org.autojs.plugin.PINYIN` action (category `pinyin`) に応答し, AIDL インターフェース `IPinyinPlugin` を通じて 5 つのメソッドを公開します; `convert` と `fromPhrase` は 2 次元配列を JSON 文字列で返し, オプションは `Bundle` で渡されます (キー: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). カスタム辞書には `pinyin.customDictionary.v1` capability が必要です. サービスと `WakeActivity` はいずれも `org.autojs.permission.PLUGIN` 権限で保護され, サードパーティアプリから直接呼び出せません.

******

### 開発ロードマップ

******

プラグインの機能計画と完了状況は, マイルストーンごとに受け入れ条件付きで整理されたチェック可能なリストとして ROADMAP.md で管理されており, 地名モード, 辞書の進化, カスタム辞書, パフォーマンス最適化, 継続的インテグレーションなどの方向を扱います. 未チェックの項目は計画中の意向であり現行バージョンの機能ではありません. Issues での議論を歓迎します.

- [ROADMAP.md を見る](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### リリース履歴

******

#### v1.0.2

_2026/09/13_

- `修正` ビルド環境の言語にかかわらずプラグインのバージョン日付を英語で表示
- `改善` 多言語リソースの統一, プラグイン有効化の明確化, リリース成果物の検証

#### v1.0.1

_2026/09/11_

- `ヒント` 本バージョンはドキュメントと関連ツーリングの改善のみで, ピンイン変換の動作とすべてのスクリプト API は変わりません
- `改善` 10 言語の README を再構成: 使用方法, クイックスタート, ピンインスタイルとオプションの早見表, スクリプト API, セルフチェック, よくある質問, 権限とセキュリティ, 姉妹プラグインの比較, プラグインインターフェースなどの章を追加
- `改善` ドキュメント生成スクリプトを同系プラグインで統一された実装へ更新: `--check` によるドリフト検出, 言語間のキーと形状の整合検証, 全角記号の拒否, バージョン整合検証をサポート
- `改善` プラグインセンターの使用説明 (`plugin_instruction.md`) を同じ多言語 JSON 生成パイプラインに統合し, 二重ソースの保守を解消
- `改善` ROADMAP.md 開発ロードマップを新設し, 姉妹プラグイン Pinyin4j との双方向リンクと選定比較を確立
- `改善` README のレイアウトと Gradle プラットフォームのバージョン管理方式を統一
- `改善` 意図しないネイティブ依存関係をビルド時に拒否し, JSON レポートを生成

#### v1.0.0

_2026/07/15_

- `機能` Pinyin プラグインサービス: プラグイン ID は `pinyin` で, AutoJs6 が `org.autojs.plugin.PINYIN` により自動検出して呼び出し
- `機能` ピンイン変換 API: `pinyin.convert(text, options)` は `compact()` 組み合わせメソッド付きの 2 次元候補配列を返し, `pinyin.simple(text)` はコンパクトな文字列を返却
- `機能` 辞書照会 API: `pinyin.fromCodePoint(codePoint)` は単漢字の読みレコードを, `pinyin.fromPhrase(phrase)` はフレーズの読みを照会
- `機能` 6 種類のピンインスタイル (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) と姓氏モード (`SURNAME`)
- `機能` 多音字と単語分割のサポート: 単漢字, フレーズ, 単語分割の 3 つの辞書と HMM モデルを内蔵し, 必要に応じて `segment` / `heteronym` / `group` オプションを有効化可能
- `機能` 多言語リソース: プラグイン情報と使用説明が 10 言語をカバー
- `機能` README と CHANGELOG は JSON ソースファイルと `.python/generate_markdown.py` から多言語 Markdown を生成

##### その他のリリース履歴は以下を参照

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-ja.md)

******

### ビルド

******

この節はソースからプラグインをビルドしたい開発者向けです.

debug APK をビルド:

```powershell
.\gradlew.bat :app:assembleDebug
```

JVM 単体テストを実行し instrumentation テスト APK をビルド:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

release APK をビルド (単一の汎用パッケージ; バージョン管理外の `sign.properties` に署名を設定すると自動署名されます):

```powershell
.\gradlew.bat :app:assembleRelease
```

1 つのコマンドで署名済み universal APK をビルドして検証し, 英語 CHANGELOG から `SHA256SUMS.txt` と `RELEASE_NOTES.md` を生成:

```powershell
py scripts\release\prepare_release.py
```

多言語ドキュメントのソースと生成物が同期しているかを検証 (CI でも実行されます):

```powershell
py .python\generate_markdown.py --check
```

ビルドパラメータは `version.properties` に集約されています: 最小 SDK 24 (Android 7.0), ターゲット SDK 36, 現在のバージョン 1.0.2.

******

### ローカライズとドキュメント生成

******

```text
.readme/common.json
.readme/lang_*.json
.readme/template_readme.md
.readme/template_plugin_instruction.md
.changelog/lang_*.json
.changelog/template_changelog.md
.python/generate_markdown.py
app/src/main/assets/doc/CHANGELOG-*.md
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

`strings.xml` はローカライズされたプラグイン説明を, `plugin_instruction.md` はホストのプラグインセンターに表示される使用説明を提供します. README, 更新履歴, 使用説明はすべて JSON ソースから生成されます: `.readme/` と `.changelog/` 配下のソースを編集した後, `py .python/generate_markdown.py` を実行して全成果物を再生成してください. 生成物は手動で編集しません; `py .python/generate_markdown.py --check` でソースと成果物の同期を検証できます.

******

### ライセンス

******

プロジェクトコードは [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE) の下でライセンスされています. 内蔵の単語分割実装は [jieba-analysis](https://github.com/huaban/jieba-analysis) プロジェクトから移植したもので, API 設計は [pinyin](https://github.com/hotoo/pinyin) ライブラリに合わせています.

******

### 関連リンク

******

- AutoJs6 Pinyin ドキュメント: https://docs.autojs6.com/#/pinyin
- AutoJs6 プロジェクト: https://github.com/SuperMonster003/AutoJs6
- 姉妹プラグイン Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- pinyin ライブラリ (API 設計の参考): https://github.com/hotoo/pinyin
- jieba-analysis プロジェクト: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
