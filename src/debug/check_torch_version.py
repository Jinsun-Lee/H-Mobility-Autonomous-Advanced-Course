# 2024-07 H-mobility, Jinsun Lee

import torch
import torchvision

# PyTorch와 torchvision의 호환성 확인 매트릭스
compatibility_matrix = {
    "1.9.0": ["0.10.0"],
    "1.9.1": ["0.10.0"],
    "1.10.0": ["0.11.0"],
    "1.10.1": ["0.11.2"],
    "1.11.0": ["0.12.0"],
    "1.12.0": ["0.13.0"],
    "1.12.1": ["0.13.1"],
    "1.13.0": ["0.14.0"],
    "1.13.1": ["0.14.1"],
    "2.0.0": ["0.15.0"],
    "2.0.1": ["0.15.1"],
    "2.1.0": ["0.16.0"],
    "2.1.1": ["0.16.1"],
    "2.1.2": ["0.16.2"],
    
    # 최신 버전 추가 필요 https://github.com/pytorch/vision#installation
} 


# GPU나 CPU 타입 중 버전 정보만 추출
def version_extracted(full_version):
    #torch_version = ".".join(torch_version.split(".")[:3])
    before_plus = full_version.split("+")[0].split(".")
    only_version = ".".join(before_plus[:3])
    return only_version



# 현재 버전이 호환되는지 확인
def check_compatibility(torch_version, torchvision_version, compatibility_matrix):
    
    if torch_version in compatibility_matrix:
        if torchvision_version in compatibility_matrix[torch_version]:
            print("PyTorch and torchvision versions are compatible.")
        else:
            print("PyTorch and torchvision versions are NOT compatible.")
            # You need check: https://pytorch.org/get-started/previous-versions/
    else:
        print("PyTorch version not found in the compatibility matrix.")
        


if __name__ == '__main__':
    
    # 현재 설치된 버전 확인
    torch_version = torch.__version__
    torchvision_version = torchvision.__version__
    
    # 전체 버전 정보 출력 
    print(f"PyTorch version: {torch_version}")
    print(f"torchvision version: {torchvision_version}")
    
    torch_version = version_extracted(torch_version)
    torchvision_version = version_extracted(torchvision_version)
        
    check_compatibility(torch_version, torchvision_version, compatibility_matrix)
