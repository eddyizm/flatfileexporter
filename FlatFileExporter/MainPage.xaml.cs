using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Win32;
using System.Windows;
using System.Windows.Controls;
using System.Diagnostics;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for MainPage.xaml
    /// </summary>
    public partial class MainPage : Page
    {
        

        public MainPage()
        {
            InitializeComponent();
            

        }

        private void BtnGenerateFile_Click(object sender, RoutedEventArgs e)
        {
            // this needs to be wrapped into a seperate function and possibly class.
            var folder = Environment.CurrentDirectory;
            var ff_cli = System.IO.Path.Combine(folder, "Resources\\flatfile_cli.exe");
            MessageBox.Show(ff_cli);
            ProcessStartInfo processStartInfo = new ProcessStartInfo(ff_cli);
            Process p = Process.Start(processStartInfo);
            p.WaitForExit();
        }

        private void BtnOpenFile_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            openFileDialog.ShowDialog();
        }

        private void BtnClear_Click(object sender, RoutedEventArgs e)
        {
            // this does nothing apparently.
            NavigationService.Refresh();

        }

        private void btnAddServer_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = Application.Current.Windows.OfType<MainWindow>().FirstOrDefault();
            if (mw != null)
                mw._mainFrame.Content = new ServerPage();
                
        }
    }
}
