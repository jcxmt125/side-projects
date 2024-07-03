addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request))
  })
  
  async function handleRequest(request) {
    const url = new URL(request.url)
    const path = url.pathname
  
    // Redirectable URLs
    const redirectUrls = [
      `https://example.com${path}`,
    ]
  
    const commonExts = [
      ``,
      `.mp4`,,
      `.pdf`,
      `.webp`,
      `.avif`,
      `.jpg`
    ]
  

    // I don't completely understand this code as it was written with AI
    for (const redirectUrl of redirectUrls) {
      for (const ext of commonExts) {
        const controller = new AbortController();
        const signal = controller.signal;
  
        const fullUrl = redirectUrl + ext
        try {
          const response = await fetch(fullUrl, { signal });
          if (response.ok) {
            controller.abort(); // Abort any remaining fetches
            return Response.redirect(fullUrl, 301);
          }
        } catch (error) {
          if (error.name !== 'AbortError') {
            // Handle other errors (like network issues)
            console.error('Error fetching:', fullUrl, error);
          }
        }
      }
    }
  
    // If none of the redirect URLs work, return the original request (404)
    return new Response(
      'Resource not found. Finder may not have searched for the correct extension, or there may have been a typo.', {status: 404, statusText: 'Resource not found.'}
    )
  }
  