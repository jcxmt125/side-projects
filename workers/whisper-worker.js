export default {
    async fetch(request, env) {
      const fileUrl = request.headers.get("fileUrl");
      const authKey = request.headers.get("authKey");
  
      if (!authKey){
        return new Response('Missing key', { status: 401 });
      }
  
      if (!fileUrl) {
        return new Response('Missing fileUrl parameter', { status: 400 });
      }
      
      if (!(authKey==="[Your Unique Key]")){
        return new Response('Invalid key', {status:401})
      }
  
      const audioResponse = await fetch(
        fileUrl
      );
      const blob = await audioResponse.arrayBuffer();
  
      const inputs = {
        audio: [...new Uint8Array(blob)]
      };
      const response = await env.AI.run('@cf/openai/whisper', inputs);
  
      return Response.json({ response });
    }
  };
  