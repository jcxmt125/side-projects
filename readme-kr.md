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
- htmlify.py: 원하는 텍스트가 포함된 source.txt 파일을 만들면, 줄넘김을 \<br\>로 변환해주고, 탭을 적용해줍니다.
- trpg-helper.py: TRPG 세션을 도와주는 파이썬 스크립트. 현재 커스텀 룰셋의 클레릭을 위해 만들어져 있습니다.
- create-3d-trangles.py: a-frame 환경에서 디스플레이 가능한, 여러 색의 삼각형을 만들어주는 스크립트.
- uploadfile.py: 이 파일은 S3 / Backblaze사의 B2 저장공간에 대한 *아주* 간단한 터미널 기반 UI를 제공합니다.
- webNowPlayingLogger.py: 현재 재생중인 음악과 아티스트 정보를 파일에 로깅합니다.
- wnpLogRead.py: (위 파일을 읽는걸 도와줍니다)
- gemini-api-multimodal.py: Gemini API에 사진을 보내 분석을 요청합니다.
- mc-serverdeploy.py: (이 파일에 대한 설명은 웹사이트를 참고해주세요)
- llm-comparison.py: 무작위 AI와 연결해주고, 채팅이 끝난 뒤 알려줍니다.
- mcs-deploy-config series: Helps you deploy a minecraft server. See site for more info.

You might want to look at the requirements in the file before running them.

## The musicLab directory

This is where songs I made for fun reside!
It was made in [Song Maker Plus](https://www.songmakerpl.us/), which allows anyone to create songs.
To listen to them, you could try playing the MIDI file directly, or see more [here](https://hackclub.jclink.link/documentations/music.html).

더 자세한 안내를 위해선, [웹사이트를 방문해주세요!](https://ghpages.jclink.link/documentations/index.html)