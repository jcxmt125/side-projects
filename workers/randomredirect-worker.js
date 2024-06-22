export default{
  
    fetch(request){
      const url = new URL(request.url);
      const path = url.pathname;
      if (path === "/"){
        const urls = [
          // Where to redirect users to if they visit the root domain
        ];
        const randomIndex = Math.floor(Math.random() * urls.length);
        const redirectUrl = urls[randomIndex];
        return Response.redirect(redirectUrl.toString(), 302);
      }
      
      if (path === "/path1"){//change the path!
        const urls = [
          // Where to redirect users to if thy visit ".../path1"
        ];
        const randomIndex = Math.floor(Math.random() * urls.length);
        const redirectUrl = urls[randomIndex];
        return Response.redirect(redirectUrl.toString(), 302);
      }

      //copy paste more for more paths
      
      return new Response("Incorrect parameter",{status:404})
      //404 if the thing isn't on the list
      
      
    },
      
  };