export default async function handler(req,res){

 const url = req.query.url;

 if(!url){
   return res.json({error:"missing url"});
 }

 const api =
 "https://yeumoney.com/QL_api.php"+
 "?token=d754503b7998d34db1e601738a0934fca7dbd20a72fdd615ecabcf6a6919a14a"+
 "&format=text"+
 "&url="+encodeURIComponent(url);

 const r = await fetch(api);
 const text = await r.text();

 res.json({
   short: text.trim()
 });
}
