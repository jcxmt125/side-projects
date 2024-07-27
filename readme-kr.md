# 아무거나 모아놓은 side-projects 프로젝트!

## 그래서 이게 뭐라고요?

제 사이드 프로젝트 (잡것들)을 모아둔 디렉토리에요.
여깄는건 작동할 수도 있어요.
안할 수도 있고요. 저도 사실 잘 몰라요.
제 실험적인 내용을 모두 모아둔 리포지토리에요!

## workers 디렉토리

Cloudflare Workers 플랫폼에서 사용 가능한 코드 모음이에요.
Workers 웹 에디터로 코드를 붙여넣으면 작동할거에요! 아마.

- helloworld-worker.js: *hello world*를 리턴하는 API를 만듭니다. GET 요청을 보내보세요!
- Whisper-worker.js: 기존 템플릿의 수정본입니다! 원래의 Whisper 템플릿에서 배포해야 바인딩이 정상적으로 처리됩니다... (해봤어요. 진짜 안돼요.) "fileUrl"과, authKey 헤더를 설정해 GET 요청을 보내보세요. 너무 큰 파일은 무료 티어에선 처리할 수 없어요.
- randomredirect-worker.js: 사람들을 랜덤한 URL로 302 리디렉 시킵니다!
- finder-worker.js: 여러 온라인 저장소에서 파일을 찾아줍니다!
- create-3d-triangles-workers.py: [웹사이트 내용을 참고해주세요]

## 파이썬 스크립트 디렉토리

여러 파이썬 코드가 있어요!

- ...-worker-test.py: 위의 워커들을 테스트하는데에 사용됩니다.
- htmlify.py: make a source.txt file with the content you want and it should convert all newlines to a \<br\> tag, and tab out things.
- trpg-helper.py: a file to help you out for TRPG sessions. Currently adapted to me and my friend's ruleset for a cleric.
- create-3d-trangles.py: a file that makes a txt file containing randomly colored, circularly-placed triangles and tetrahedrons for use in an a-frame environment.
- uploadfile.py: a file that provides a *very* simple Terminal-based UI to upload files to a S3 compatible storage or Backblaze B2 (Warning: dynamic imports!)
- webNowPlayingLogger.py: logs the playing song an artist to a file
- wnpLogRead: helps read said file
- gemini-api-multimodal: Lets you ask Gemini about images
- mc-serverdeploy.py: See website for guide on using this file.
- llm-comparison.py: Makes you chat to a random chatbot, and reveals who it was when the chat ends.
- mcs-deploy-config series: Helps you deploy a minecraft server. See site for more info.

You might want to look at the requirements in the file before running them.

For more information, [visit my website!](https://hackclub.jclink.link/documentations)

## The musicLab directory

This is where songs I made for fun reside!
It was made in [Song Maker Plus](https://www.songmakerpl.us/), which allows anyone to create songs.
To listen to them, you could try playing the MIDI file directly, or see more [here](https://hackclub.jclink.link/documentations/music.html).