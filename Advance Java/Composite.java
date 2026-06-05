import java.util.ArrayList;
import java.util.List;

interface FileSystemNode {
    void showDetails(String indent);
    int getSize();
}

class FileItem implements FileSystemNode {
    private final String name;
    private final int size;

    public FileItem(String name, int size) {
        this.name = name;
        this.size = size;
    }

    @Override
    public void showDetails(String indent) {
        System.out.println(indent + "- File: " + name + " (" + size + " KB)");
    }

    @Override
    public int getSize() {
        return size;
    }
}

class Folder implements FileSystemNode {
    private final String name;
    private final List<FileSystemNode> children = new ArrayList<>();

    public Folder(String name) {
        this.name = name;
    }

    public void add(FileSystemNode node) {
        children.add(node);
    }

    public void remove(FileSystemNode node) {
        children.remove(node);
    }

    @Override
    public void showDetails(String indent) {
        System.out.println(indent + "+ Folder: " + name + " [Total Size: " + getSize() + " KB]");
        for (FileSystemNode child : children) {
            child.showDetails(indent + "   ");
        }
    }

    @Override
    public int getSize() {
        int total = 0;
        for (FileSystemNode child : children) {
            total += child.getSize();
        }
        return total;
    }
}

public class CompositeDemo {
    public static void main(String[] args) {
        FileSystemNode resume = new FileItem("Resume.pdf", 120);
        FileSystemNode photo = new FileItem("Photo.png", 350);
        FileSystemNode song = new FileItem("Song.mp3", 5000);
        FileSystemNode notes = new FileItem("Notes.txt", 
