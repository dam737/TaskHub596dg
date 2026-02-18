export default async function handler(req, res) {

  const { url } = req.query;

  if (!url) {
    res.status(400).json({ error: "missing url" });
    return;
  }

  const token = "d754503b7998d34db1e601738a0934fca7dbd20a72fdd615ecabcf6a6919a14a";

  const api =
    `https://yeumoney.com/QL_api.php?token=${token}&format=text&url=${encodeURIComponent(url)}`;

  try {
    const r = await fetch(api);
    const text = await r.text();

    res.status(200).json({
      short: text.trim()
    });

  } catch (e) {
    res.status(500).json({ error: "api failed" });
  }
}
