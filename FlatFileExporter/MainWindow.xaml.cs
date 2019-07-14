﻿using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Resources;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;


namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            PopulateServerItems();
        }

        private void Menu_Exit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }

        
        private void BtnOpenFile_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            openFileDialog.ShowDialog();
        }

        private void PopupBox_Closed(object sender, RoutedEventArgs e)
        {

        }

        private void PopupBox_Opened(object sender, RoutedEventArgs e)
        {

        }

        private void BtnAddServer_Click(object sender, RoutedEventArgs e)
        {

        }

        private void BtnGenerateFile_Click(object sender, RoutedEventArgs e)
        {
            // this needs to be wrapped into a seperate function and possibly class.
            var folder = Environment.CurrentDirectory;
            var ff_cli = Path.Combine(folder, "Resources\\flatfile_cli.exe");
            MessageBox.Show(ff_cli);
            ProcessStartInfo processStartInfo = new ProcessStartInfo(ff_cli);
            Process p = Process.Start(processStartInfo);
            p.WaitForExit();
        }

        private void BtnClear_Click(object sender, RoutedEventArgs e)
        {

        }

        // combo box populate
        public ObservableCollection<ComboBoxItem> cbServerItems { get; set; }
        public ComboBoxItem SelectedcbServerItem { get; set; }
        private void PopulateServerItems()
        {
            DataContext = this;
            cbServerItems = new ObservableCollection<ComboBoxItem>();
            var cbServerItem = new ComboBoxItem { Content = "<--Select-->" };
            SelectedcbServerItem = cbServerItem;
            cbServerItems.Add(cbServerItem);
            cbServerItems.Add(new ComboBoxItem { Content = "Option 1" });
            cbServerItems.Add(new ComboBoxItem { Content = "Option 2" });
        }
        
    }
}
