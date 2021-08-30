import cv2


def images_to_video():
    fps = 60  # 帧率
    num_frames = 120
    img_array = []
    img_width = 1280
    img_height = 720
    for i in range(num_frames + 1):
        print(i,'step1')
        filename = "D:/Scientific Research/source/frame" + str(i) + ".jpg"
        img = cv2.imread(filename)

        if img is None:
            print(filename + " is non-existent!")
            continue
        img = img[720:1440,1280:2560]
        img_array.append(img)

    out = cv2.VideoWriter('D:/Scientific Research/target/demo.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (img_width, img_height))

    for i in range(len(img_array)):
        print(i,'step2')
        out.write(img_array[i])
    out.release()


def main():
    images_to_video()


if __name__ == "__main__":
    main()







