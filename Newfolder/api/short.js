export default async function handler(req, res) {

 const url=req.query.url;

 if(!url){
  return res.status(400).json({error:"missing url"});
 }

 const TOKEN="YOUR_YEUMONEY_TOKEN";

 const api=
 "https://yeumoney.com/QL_api.php"
 +"?token="+TOKEN
 +"&format=json"
 +"&url="+encodeURIComponent(url);

 try{

  const r=await fetch(api);
  const data=await r.json();

  res.status(200).json(data);

 }catch(e){
  res.status(500).json({error:"api error"});
 }
}
